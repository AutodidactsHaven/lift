import os

from lift.lift_class import LiftClass
import lift.print_color as Out

def setup(lift):
    # Project settings
    lift.app_name = "app"
    lift.dir_root = os.getcwd();
    lift.dir_source = "/src"
    lift.dir_build = "/build"
    lift.dir_libs = ""
    lift.dir_include = ""
    lift.libs = ""

    # Compiler settings
    lift.compiler = "clang"
    lift.flags_debug = lift.flags_default("debug")
    lift.flags_release = lift.flags_default("release")

    # Incremental compilation settings
    lift.incremental_compilation = True

    # Compilation & Linker settings
    lift.threads = 8
    
    return lift


def build(mode):
    Out.print_debug("Running build()")

def run():
    Out.print_debug("Running run()")

def clean():
    Out.print_debug("Running clean()")

def test():
    Out.print_debug("Running test()")
    





if __name__ == "__main__":
    Out.print_error("This scipt is not designed do be executed with Python itself, its part of the lift build system")
