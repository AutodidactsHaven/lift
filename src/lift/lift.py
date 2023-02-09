import sys
from lift.color import COLOR
from lift.color import STYLE

# Global vars
DEBUG = True


def lift_print(text):
    print(f"{STYLE.DEFAULT}{text}{COLOR.RESET}")


def lift_print_debug(text):
    print(f"{STYLE.DEBUG}{text}{COLOR.RESET}")


def main():
    lift_print("lift")
    if DEBUG:
        lift_print_debug(f"{len(sys.argv)} argv variables passed:")
        for i in sys.argv:
            lift_print_debug(i)


if __name__ == "__main__":
    main()
