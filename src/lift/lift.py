import sys
from lift.color import COLOR
from lift.color import STYLE
from lift.cli import CLI


def lift_print(text):
    print(f"{STYLE.DEFAULT}{text}{COLOR.RESET}")


def lift_print_error(text):
    print(f"{STYLE.ERROR_TAG}ERROR:{COLOR.RESET}{STYLE.ERROR} {text}{COLOR.RESET}")


def lift_print_debug(text):
    print(f"{STYLE.DEBUG_TAG}DEBUG:{COLOR.RESET}{STYLE.DEBUG} {text}{COLOR.RESET}")


def main():
    lift_print("lift")

    # if no argument is provided then print help
    if len(sys.argv) < 2:
        lift_print_debug("TODO: Help section")
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
                lift_print_error(
                    f"{cli_parameter} is not a valid parameter for {cli_action}")
                exit()
    else:
        lift_print_error(f"{cli_action} is not a valid key")
        exit()


if __name__ == "__main__":
    main()
