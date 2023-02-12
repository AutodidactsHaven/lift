from lift.lift import Lift

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

    # Compiler settings
    compiler = "gcc"
    flags_debug = lift.flags_debug_default()
    flags_release = lift.flags_release_default()

    # Incremental compilation settings
    incremental_compilation = True

    # Compilation & Linker settings
    threads = 8

    def __init__(self):
        # default LiftClass constructor
        # TODO: Load preference for gcc/clang from config
