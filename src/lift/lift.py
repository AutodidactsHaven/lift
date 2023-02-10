import os
import sys
import importlib.util

import lift.print_color as out
import lift.lift_build_default as lift_build

def main():
    out.print_info("- - - lift - - -")

    # Working dir which lift was called from, must contain lift_build.py
    working_dir = os.getcwd()
    lift_build_path = working_dir + "/lift_build.py"
    if not os.path.isfile(lift_build_path):
        out.print_error("lift_build.py is used")
        exit()

    # Load the module using import_module
    spec = importlib.util.spec_from_file_location("lift_build", lift_build_path)
    lift_build = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lift_build)


    # CLI parsing
    if len(sys.argv) < 2:
        out.print_help()
        exit()

    lift_build.build("debug")

#    # if no argument is provided then print help
#    if len(sys.argv) < 2:
#        out.print_debug("TODO: Help section")
#        # TODO: lift executed without parameters, print help
#        exit()
#
#    # extract cli_action and cli_parameter from arguments
#    cli_action = sys.argv[1]
#    cli_parameter = None
#    if len(sys.argv) > 2:
#        cli_parameter = sys.argv[2]
#
#    # check if cli_action and cli_parameter are valid
#    if cli_action in CLI.actions:
#        if cli_parameter:
#            if not (cli_parameter in CLI.parameters) or (cli_action == CLI.actions.get("add")):
#                # TODO: Handle add key, since any name of the lib can follow
#                out.print_error(
#                    f"{cli_parameter} is not a valid parameter for {cli_action}")
#                exit()
#        # switch case of cli_action and cli_parameter pairs
#        if cli_action == CLI.init:
#            out.print_info("init")
#        elif cli_action == CLI.debug or cli_action == CLI.release:
#            # something to do with build or build&run
#            if cli_parameter == CLI.build or cli_parameter == CLI.run:
#                out.print_info(f"{cli_action} -> {cli_parameter}")
#                if cli_action == CLI.debug:
#                    BUILD.build(COMPILER.DEBUG);
#                else:
#                    BUILD.build(COMPILER.RELEASE);
#                if cli_parameter == CLI.run:
#                    BUILD.run();
#            else:
#                out.print_error("Incorect argument")
#                out.print_info("use: lift debug/release build/run")
#        elif cli_action == CLI.test:
#            out.print_info("test")
#        elif cli_action == CLI.clean:
#            out.print_info("clean")
#        elif cli_action == CLI.add:
#            out.print_info("add")
#        elif cli_action == CLI.help:
#            out.print_info("help")
#    else:
#        out.print_error(f"{cli_action} is not a valid key")
#        exit()

    #files = FILES("sample")
    #out.print_info(files.all_files)
    #out.print_info(files.get_build())
    #out.print_info(files.get_files_with_exensions({".h",".c"}));

    #flags = COMPILER(COMPILER.CLANG).generate_flags(COMPILER.DEBUG)
    #out.print_info(flags)


if __name__ == "__main__":
    main()
