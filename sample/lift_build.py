# Lift build system config script
import os
import sys
import lift.print_color as Out
from lift.files import Files
from lift.compiler import Compiler
from lift.workers import Workers

# Toggle on/off printing of out.print_debug
Out.TOGGLE_DEBUG = True 

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

    ### Finding files
    Out.print_info("> Finding source files")
    # get all files in path_src
    path_src_files = Files(project_settings["path_src"])
    # exclude files which are not *.h and *.c 
    path_src_source = path_src_files.get_files_with_exensions({".h",".c"})
    Out.print_debug(path_src_source)

    ### Compiler setup
    Out.print_info("> Compiler setup")
    comp = Compiler(project_settings["compiler"])
    flags = comp.generate_flags(mode)

    ### Dependancy graph
    # TODO
    
    ### Generating object files
    Out.print_info("> Generating *.o files")
    workers_gen_o = Workers()
    jobs = ["--version"]
    for file in path_src_source:
        if not file.endswith(".c"):
            continue
        working_dir = project_settings["working_dir"]
        o_file_name = file.split("/")[-1].replace(".c", ".o")
        o_file = f"{working_dir}/build/{o_file_name}"
        jobs.append(f"{flags} -c '{file}' -o '{o_file}'")
    which_compiler = project_settings["compiler"].lower()
    workers_gen_o.work(which_compiler, jobs)


def run():
    Out.print_debug("Running run()")

def clean():
    Out.print_debug("Running clean()")

def test():
    Out.print_debug("Running test()")
    





if __name__ == "__main__":
    Out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
