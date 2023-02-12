# Lift build system config script
import os
import sys
import time
import lift.print_color as Out
from lift.files import Files
from lift.compiler import Compiler
from lift.workers import Workers
from lift.incremental import FileModifiedCache

# Toggle on/off printing of out.print_debug
Out.TOGGLE_DEBUG = False

project_path = os.getcwd()
project_settings = {
    "executable_name": "app",
    # supported: "GCC", "CLANG"
    "compiler": "CLANG",
    "working_dir": project_path,
    "path_src": project_path + "/src",
    "build_path": project_path + "/build", 
    }

# build mode can be RELEASE/DEBUG 
def build(mode):
    Out.print_debug("Running build()")

    ### Vars
    which_compiler = project_settings["compiler"].lower()
    executable_name =  project_settings.get("build_path") + "/" +  project_settings.get("executable_name")

    ### Makind necessary dirs
    if not os.path.exists(project_settings.get("build_path")):
        os.mkdir(project_settings.get("build_path"))

    ### Finding source files
    Out.print_info("> Finding source files")
    # get all files in path_src
    path_src_files = Files(project_settings["path_src"])
    # exclude files which are not *.h and *.c 
    path_src_source = path_src_files.get_files_with_extensions({".h",".c"})
    Out.print_debug(path_src_source)

    ### Compiler setup
    Out.print_info("> Compiler setup")
    comp = Compiler(project_settings["compiler"])
    flags = comp.generate_flags(mode)

    ### mtime cache
    Out.print_info("> Resolve incremental compilation")
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
    # TODO

    # get object files that exist
    build_files = Files(project_settings["build_path"]).get_files_with_extensions({".o"})
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
    print(uncompiled_source_files)

    # Files to compile are set of incremental compilation targets and uncompiled source files
    source_files_to_compile = path_src_source

    ### Generating object files
    Out.print_info("> Generating *.o files")
    workers_gen_o = Workers()
    o_jobs = []
    for file in source_files_to_compile:
        if not file.endswith(".c"):
            continue
        working_dir = project_settings["working_dir"]
        o_file_name = file.split("/")[-1].replace(".c", ".o")
        o_file = f"{working_dir}/build/{o_file_name}"
        o_jobs.append(f"{flags} -c '{file}' -o '{o_file}'")
    workers_gen_o.work(which_compiler, o_jobs)

    ### Linking into executable
    Out.print_info("> Linking *.o files into executable")
    workers_gen_exe = Workers()
    o_files_dir = Files(project_settings["build_path"])
    o_files_list = o_files_dir.get_files_with_extensions({".o"})
    o_files = ""
    for file in o_files_list:
        o_files += f" '{file}' "
    job = [f"{flags} {o_files} -o '{executable_name}'"]
    workers_gen_exe.work(which_compiler, job)


def run():
    Out.print_debug("Running run()")

def clean():
    Out.print_debug("Running clean()")

def test():
    Out.print_debug("Running test()")
    





if __name__ == "__main__":
    Out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
