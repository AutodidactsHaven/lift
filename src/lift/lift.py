import sys
from lift.color import COLOR
from lift.color import STYLE
from lift.cli import CLI
from lift.compiler import COMPILER
from lift.files import FILES
import lift.print as out

def main():
    out.print_info("lift")

    # if no argument is provided then print help
    if len(sys.argv) < 2:
        out.print_debug("TODO: Help section")
        # TODO: lift executed without parameters, print help
        exit()

    # extract cli_action and cli_parameter from arguments
    cli_action = sys.argv[1]
    cli_parameter = None
    if len(sys.argv) > 2:
        cli_parameter = sys.argv[2]

    # check if cli_action and cli_parameter are valid
    if cli_action in CLI.actions:
        if cli_parameter:
            if cli_parameter in CLI.parameters or cli_action == CLI.actions.get("add"):
                print("")
            else:
                out.print_error(
                    f"{cli_parameter} is not a valid parameter for {cli_action}")
                exit()
    else:
        out.print_error(f"{cli_action} is not a valid key")
        exit()


    files = FILES("sample")
    out.print_info(files.all_files)
    out.print_info(files.get_build())
    out.print_info(files.get_files_with_exensions({".h",".c"}));

    flags = COMPILER(COMPILER.CLANG).generate_flags(COMPILER.DEBUG)
    out.print_info(flags)


if __name__ == "__main__":
    main()
