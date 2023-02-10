import lift.print as out
from lift.files import FILES

class BUILD:
    def build():
        # Figure out which files we need to build
            # find all source files
            # find all .o files
            # compare timestamps
        # Build dependency graph for files we need to build
        # Generate compiler commands for making .o files
        # Feed compiler commands into threading system
        # Link .o into executable

        src_files = FILES("sample") # TODO: Change to SRC, then change to lift_bulid.py var
        out.print_debug(src_files.get_files_with_exensions({".h",".c"}));

        o_files = FILES("build")    
        out.print_info("Building the application");

    def run():
        out.print_info("Running the application")
