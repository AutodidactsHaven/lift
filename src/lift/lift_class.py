import os
import shutil
import lift.print_color as Out
from lift.compiler import Compiler
from lift.files import Files
from lift.workers import Workers

class LiftClass:
    # Name of your app
    app_name = "app"
    # Root directory of your app (contains "lift_build.py", "build/", "src/")
    dir_root = os.getcwd();
    # Sources directory (usulaly "/src")
    dir_source = "/src"
    # Build directory (usulaly "/build")
    dir_build = "/build"
    # Objects directory within build directory (usually "/object") 
    dir_object = "/object"
    # Directory for additonal libs ("-L" flag)
    dir_lib = ""
    # Directory for additonal includes ("-I" flag)
    dir_include = ""
    # List of libs (Example: "-lraylib -lX11")
    libs = ""

    # blacklist files
    file_blacklist = {""}
    # blacklist dirs
    dir_blacklist = {""}

    # Compiler settings
    compiler = "gcc"
    flags_debug = ""
    flags_release = ""
    # Incremental compilation settings
    incremental_compilation = True

    # Compilation & Linker settings
    threads = 8

    # Compiler formatting
    str_format_compiler = "{FLAGS} -c '{C_FILE}' -o '{O_FILE}'"
    str_format_linker = "{DIR_LIB} {LIBS} {DIR_INCLUDE} {FLAGS} {OBJECTS} -o '{APP_NAME}'"


    def __init__(self):
        Out.print_debug("> Generating lift_class.py->__init__")
        # default LiftClass constructor
        self.flags_debug = self.flags_default("debug")
        self.flags_release = self.flags_default("release")
        # TODO: Load preference for gcc/clang from config

    ###########################################################################

    # "release" / "debug"
    def flags_default(self, mode):
        comp = Compiler(self.compiler)
        return comp.generate_flags(mode)

    def build(self, mode):
        Out.print_debug(f"> Running LiftClass.build({mode})")
        # compile object files
        source_files = self.get_source_files()
        files_to_compile = self.get_files_filter(source_files, ".c"); # FIXME: Temporary until Omni is done
        self.compile(mode, files_to_compile)
        # remove old app executable
        self.remove_app()
        # link object files 
        objects_to_link = self.get_object_files()
        self.link(mode, objects_to_link)

    def run(self, args):
        Out.print_debug("> Running LiftClass.run()")
        app_name = self.dir_root + self.dir_build + "/" + self.app_name
        exec_args = [app_name] + args
        # Replace the current process with the executable
        os.execvp(app_name, exec_args)

    def clean(self):
        Out.print_debug("> Running LiftClass.clean()")
        path = self.dir_root + self.dir_build
        if os.path.exists(path):
            # Display the path and ask for confirmation
            response = input(f"{Out.COLOR.RED}> Delete the folder at {Out.COLOR.BLUE}{path}{Out.COLOR.RESET}? (y/n) ")
            if response.lower() == "y":
                # Remove the folder and everything inside it
                shutil.rmtree(path)
                Out.print_info(f"> Deleted folder at {path}")
            else:
                Out.print_info(f"> Cancelled deletion of folder at {path}")
        else:
            Out.print_info(f"> Folder at {path} does not exist")

    def test(self):
        Out.print_debug("> Running LiftClass.test()")

    def compile(self, mode, source_files):
        Out.print_debug(f"> Running LiftClass.compile({mode}, {source_files})")
        self.dir_makedir(self.dir_root + self.dir_build)
        self.dir_makedir(self.dir_root + self.dir_build + self.dir_object)
        # generate compiler command
        commands = []
        for file in source_files:
            o_file = self.dir_root + self.dir_build + self.dir_object + "/" + file.split("/")[-1].replace(".c", ".o")
            command = self.str_format_compiler
            command = command.replace("{FLAGS}", self.get_flags(mode))
            command = command.replace("{C_FILE}", file)
            command = command.replace("{O_FILE}", o_file)
            commands.append(command)
            Out.print_debug(command)
        # spawn workers 
        worker_manager = Workers()
        worker_manager.work(self.compiler, commands, self.threads)
        

    def link(self, mode, object_files):
        Out.print_debug(f"> Running LiftClass.link({mode}, {object_files})")
        self.dir_makedir(self.dir_root + self.dir_build)
        self.dir_makedir(self.dir_root + self.dir_build + self.dir_object)
        # Combine all objects into string
        objects = ""
        for file in object_files:
            objects += f" '{file}' "
        # generate compiler command
        app_name = self.dir_root + self.dir_build + "/" + self.app_name
        command = self.str_format_linker
        command = command.replace("{DIR_LIB}", self.dir_lib)
        command = command.replace("{LIBS}", self.libs)
        command = command.replace("{DIR_INCLUDE}", self.dir_include)
        command = command.replace("{FLAGS}", self.get_flags(mode))
        command = command.replace("{OBJECTS}", objects)
        command = command.replace("{APP_NAME}", app_name)
        Out.print_debug(command)
        # spawn workers 
        worker_manager = Workers()
        worker_manager.work(self.compiler, [command], self.threads)

    def get_source_files(self):        
        # TODO: Scanning files for #includes
        # TODO: Generating dependency graph
        # TODO: Exluding elements in (file_blacklist, dir_blacklist) from files
        Out.print_debug("> Running LiftClass.get_source_files()")
        files = Files(self.dir_root + self.dir_source)
        source_files = files.get_files_with_extensions({".c", ".h"})
        return source_files

    def get_object_files(self):
        # TODO: Exluding elements in (file_blacklist, dir_blacklist) from .o files
        # if program was compiled eariles without those filters, these .o files still
        # might exist and become part of the executable by accident.
        Out.print_debug("> Running LiftClass.get_object_files()")
        files = Files(self.dir_root + self.dir_build + self.dir_object)
        object_files = files.get_files_with_extensions({".o"})
        return object_files 

    def get_files_filter(self, files, extension):
        file_list = []
        for file in [f for f in files if f.endswith(extension)]:
            file_list.append(file)
        return file_list

    def get_flags(self, mode):
        if mode == "debug":
            return self.flags_debug
        else:
            return self.flags_release

    # make dir if it does not exist
    def dir_makedir(self, directory):
        if not os.path.exists(directory):
            os.mkdir(directory)

    def remove_app(self):
        app_name = self.dir_root + self.dir_build + "/" + self.app_name
        if os.path.exists(app_name):
            os.remove(app_name)
