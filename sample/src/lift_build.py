# Lift build system config script
import os
import sys
import lift.print_color as out

# Toggle on/off printing of out.print_debug
out.TOGGLE_DEBUG = True 

project_settings = {
    "executable_name": "app",
    # GCC / CLANG are supported
    "compiler": "GCC",
    "working_dir": os.getcwd(),
    "path_src": "/src",
    "build_path": "/build", 
    }

def build(mode):
    out.print_debug("Local lift_build.py is executed")


if __name__ == "__main__":
    out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
