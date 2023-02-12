import os
import sys
import importlib.util

import lift.print_color as Out
import lift.lift_build_default as lift_build
import lift.helpers as helpers

def main():
    Out.print_info("- - - lift - - -")

    # Working dir which lift was called from, must contain lift_build.py
    lift_build_path = helpers.get_lift_build_path()
    if not os.path.isfile(lift_build_path):
        Out.print_error("lift_build.py is used")
        exit()

    # Load the module using import_module
    spec = importlib.util.spec_from_file_location("lift_build", lift_build_path)
    lift_build = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(lift_build)


    # CLI parsing
    if len(sys.argv) == 1:
        Out.print_help()
        exit()

    first_argument = sys.argv[1]
    second_argument = None
    if len(sys.argv) >= 3:
        second_argument = sys.argv[2]
    if first_argument == "init":
        Out.print_info("> init")
        # TODO: Init code for creating lift.build.py
    elif first_argument == "build" or first_argument == "run":
        # build mode selection
        if second_argument == "release":
            Out.print_info("> lift_build.py->build(\"RELEASE\")")
            lift_build.build("RELEASE")
        else:
            Out.print_info("> lift_build.py->build(\"DEBUG\")")
            lift_build.build("DEBUG")
        # run the app's executable
        if first_argument == "run":
            Out.print_info("> lift_build.py->run()")
            lift_build.run()
    elif first_argument == "test":
        Out.print_info("> lift_build.py->test()")
        lift_build.test()
    elif first_argument == "clean":
        Out.print_info("> lift_build.py->clean()")
        lift_build.clean()

if __name__ == "__main__":
    main()
