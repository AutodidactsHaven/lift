# Lift build system config script
import os
import sys
import lift.print_color as out

# Toggle on/off printing of out.print_debug
out.TOGGLE_DEBUG = True 

project_path = os.getcwd()
project_settings = {
    "executable_name": "app",
    # supported: "GCC", "CLANG"
    "compiler": "GCC",
    "working_dir": project_path,
    "path_src": project_path + "/src",
    "build_path": project_path + "/build", 
    }

# build mode can be release/debug
def build(mode):
    out.print_debug("Running build()")

def run():
    out.print_debug("Running run()")

def clean():
    out.print_debug("Running clean()")

def test():
    out.print_debug("Running test()")
    





if __name__ == "__main__":
    out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
