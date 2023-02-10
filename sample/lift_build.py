# Lift build system config script
import os
import sys
import lift.print_color as Out
from lift.files import Files
from lift.compiler import Compiler

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
    # get all files in path_src
    path_src_files = Files(project_settings["path_src"])
    # exclude files which are not *.h and *.c 
    pach_src_source = path_src_files.get_files_with_exensions({".h",".c"})
    Out.print_debug(pach_src_source)

    ### Compiler setup
    comp = Compiler(project_settings["compiler"])
    flags = comp.generate_flags(mode)
    Out.print_debug(flags)


def run():
    Out.print_debug("Running run()")

def clean():
    Out.print_debug("Running clean()")

def test():
    Out.print_debug("Running test()")
    





if __name__ == "__main__":
    Out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
