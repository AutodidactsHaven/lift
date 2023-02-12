import os
import lift.print_color as Out
from lift.compiler import Compiler

class LiftClass:
    # Name of your app
    app_name = "app"
    # Root directory of your app (contains "lift_build.py", "build/", "src/")
    dir_root = os.getcwd();
    # Sources directory (usulaly "/src")
    dir_source = "/src"
    # Build directory (usulaly "/build")
    dir_build = "/build"
    # Directory for additonal libs ("-L" flag)
    dir_libs = ""
    # Directory for additonal includes ("-I" flag)
    dir_include = ""
    # List of libs (Example: "-lraylib -lX11")
    libs = ""

    # blacklist files
    files_blacklist = {""}
    # blacklist dirs
    dirs_blacklist = {""}

    # Compiler settings
    compiler = "gcc"
    flags_debug = ""
    flags_release = ""
    # Incremental compilation settings
    incremental_compilation = True

    # Compilation & Linker settings
    threads = 8

    def __init__(self):
        Out.print_debug("> Generating lift_class.py->__init__")
        # default LiftClass constructor
        self.flags_debug = self.flags_default("debug")
        self.flags_release = self.flags_default("release")
        # TODO: Load preference for gcc/clang from config

    # "release" / "debug"
    def flags_default(self, mode):
        comp = Compiler(self.compiler)
        return comp.generate_flags(mode)

    def build(self, mode):
        Out.print_debug(f"> Running LiftClass.build({mode})")
        source_files = self.get_source_files()
        self.compile(mode, source_files)
        object_files = self.get_object_files()
        self.link(mode, object_files)

    def run(self):
        Out.print_debug("> Running LiftClass.run()")

    def clean(self):
        Out.print_debug("> Running LiftClass.clean()")

    def test(self):
        Out.print_debug("> Running LiftClass.test()")

    def compile(self, mode, source_files):
        Out.print_debug(f"> Running LiftClass.compile({mode}, {source_files})")

    def link(self, mode, object_files):
        Out.print_debug(f"> Running LiftClass.link({mode}, {object_files})")

    def get_source_files(self):
        Out.print_debug("> Running LiftClass.get_source_files()")

    def get_object_files(self):
        Out.print_debug("> Running LiftClass.get_object_files()")
