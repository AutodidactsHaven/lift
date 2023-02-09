from lift.color import COLOR
from lift.color import STYLE

def print_info(text):
    print(f"{STYLE.DEFAULT}{text}{COLOR.RESET}")


def print_error(text):
    print(f"{STYLE.ERROR_TAG}ERROR:{COLOR.RESET}{STYLE.ERROR} {text}{COLOR.RESET}")


def print_debug(text):
    print(f"{STYLE.DEBUG_TAG}DEBUG:{COLOR.RESET}{STYLE.DEBUG} {text}{COLOR.RESET}")

