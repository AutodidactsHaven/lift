"""
Entrypoint for incremental compilation.

Internally it uses FileModifiedCache and DependencyGraph to resolve a source directory
into a set of .c files that must be compiled into object files
"""
import os
import re
import lift.print_color as Out
from lift.file_modified_cache import FileModifiedCache
from lift.dependency_graph import DependencyGraph, FileNode
from lift.files import Files

class Incremental:
    def __init__(self):
        pass

    def resolve(self, path_src_files, build_dir):

        # exclude files which are not *.h and *.c 
        header_files = path_src_files.get_files_with_extensions({".h"})
        source_files = path_src_files.get_files_with_extensions({".c"})
        path_src_files = header_files + source_files

        cache = FileModifiedCache()
        cache.load()
        modified_files = []
        for file in path_src_files:
            mtime = os.path.getmtime(file)
            if cache.mtime_cache.get(file):
                if mtime > float(cache.mtime_cache[file]):
                    Out.print_color(Out.COLOR.BLUE, f'{file} has been modified since last compilation')
                    modified_files.append(file)

            cache.add_file(file) # update cache
        
        cache.store() # at end of compilation we should store back to disk
        
        ### Build Dependency graph
        dgraph = DependencyGraph()
        file_nodes = [ FileNode(p, os.path.basename(p)) for p in path_src_files]
        dgraph.add_nodes(file_nodes)

        for file in file_nodes:
            # parse file for includes
            f = open(file.absolute_path, "r")
            file_contents = f.read()
            includes = extract_includes(file_contents)
            resolve_header_path_for_file = lambda include: resolve_relative_header_path(file.absolute_path, include)
            absolute_path_includes = map(resolve_header_path_for_file, includes)
            for include in absolute_path_includes:
                target_node = dgraph.get_node_by_absolute_path(include)
                if target_node:
                    dgraph.add_dependency(file, target_node, directional=True)
                else:
                    # Out.print_debug(f"couldnt find {include}")
                    pass


        incremental_compile_files = set()

        for file in modified_files:
            if file.endswith('.c'):
                incremental_compile_files.add(file)
            else: # header file
                start_node = dgraph.get_node_by_absolute_path(file)
                if start_node:
                    deps = dgraph.accumulate_dependencies(start_node)
                    for dep in deps:
                        incremental_compile_files.add(dep)
                else:
                    #TODO (Josh) how to handle error here?
                    pass

        # get object files that exist
        build_files = Files(build_dir).get_files_with_extensions({".o"})
        object_files = set([os.path.splitext(os.path.basename(path))[0] for path in build_files])

        c_files = source_files
        # we need to turn them into a dict where { [key]: value } key = 'magic' and value = 'full_path/src/magic.c'
        # so that we can compare them without their paths or their extension (just the 'magic'), but after the comparison
        # we want to retain the original full path of the source file to pass to the compiler.
        # to do this we turn both into dicts, do a comparison on the keys (same as set minus operation)
        # then use those keys to get back out a set of paths via indexing into the original dict
        c_files_name_to_path_map = {os.path.splitext(os.path.basename(path))[0]: path for path in c_files}
        o_files_name_to_path_map = {os.path.splitext(os.path.basename(path))[0]: path for path in object_files}
        #files *without* a .o is the set of .c files minus the set of .o files
        difference = c_files_name_to_path_map.keys() - o_files_name_to_path_map.keys()
        uncompiled_source_files = {c_files_name_to_path_map[key] for key in difference}

        # Files to compile are set of incremental compilation targets, I,  and uncompiled source files, S (I union S)
        source_files_to_compile = uncompiled_source_files | incremental_compile_files
        
        return source_files_to_compile

def resolve_relative_header_path(src_file_abs_path, include):
    src_dir = os.path.dirname(src_file_abs_path)
    header_abs_path = os.path.abspath(os.path.join(src_dir, include))
    return header_abs_path

def extract_includes(text):
    # the regular expression pattern to match "#include"
    pattern = re.compile(r'#include\s+[<"](.*?)[>"]')

    # find all matches in the input text
    matches = re.findall(pattern, text)

    # return the list of matches
    return matches
