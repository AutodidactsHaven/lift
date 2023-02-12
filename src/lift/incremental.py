"""
Entrypoint for incremental compilation.

Internally it uses FileModifiedCache and DependencyGraph to resolve a source directory
into a set of .c files that must be compiled into object files
"""
import os
import lift.print_color as Out
from lift.file_modified_cache import FileModifiedCache
from lift.dependency_graph import DependencyGraph
from lift.files import Files

class Incremental:
    def __init__(self):
        pass

    def resolve(self, path_src_files, build_dir):

        # exclude files which are not *.h and *.c 
        path_src_source = path_src_files.get_files_with_extensions({".h",".c"})
        Out.print_debug(path_src_source)

        cache = FileModifiedCache()
        cache.load()
        Out.print_debug(cache.mtime_cache)

        for file in path_src_source:
            mtime = os.path.getmtime(file)
            if cache.mtime_cache.get(file):
                if mtime > float(cache.mtime_cache[file]):
                    Out.print_color(Out.COLOR.BLUE, f'{file} has been modified since last compilation')
            
            cache.add_file(file) # update cache
        
        cache.store() # at end of compilation we should store back to disk
        
        ### Dependency graph
        dgraph = DependencyGraph()
        incremental_compile_files = set()

        # get object files that exist
        build_files = Files(build_dir).get_files_with_extensions({".o"})
        object_files = set([os.path.splitext(os.path.basename(path))[0] for path in build_files])

        c_files = path_src_files.get_files_with_extensions({".c"})
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