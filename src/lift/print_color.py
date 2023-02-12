# Macros for printing with colored tags

TOGGLE_DEBUG = True
 
def print_normal(text):
    print(f"{COLOR.RESET}{text}")
    
def print_info(text):
    print(f"{STYLE.DEFAULT}{text}{COLOR.RESET}")

def print_error(text):
    print(f"{STYLE.ERROR_TAG}ERROR:{COLOR.RESET} {text}")

def print_debug(text):
    if TOGGLE_DEBUG:
        print(f"{STYLE.DEBUG_TAG}DEBUG:{COLOR.RESET} {text}")

def print_color(color, text):
    print(f"{color}{text}{COLOR.RESET}")

def print_help():
    print_info("> HELP PAGE")
    print_normal("FIXME: HELP PAGE is not implemented yet")
# used for colored printing, example of use
# print(f"{COLOR.BLUE}{COLOR.BG.BLACK}blue on black{COLOR.RESET} normal")
class COLOR:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    RESET = "\033[39;49m"

    class BG:
        BLACK = "\033[40m"
        RED = "\033[41m"
        GREEN = "\033[42m"
        YELLOW = "\033[43m"
        BLUE = "\033[44m"
        MAGENTA = "\033[45m"
        CYAN = "\033[46m"
        WHITE = "\033[47m"
        RESET = "\033[39;49m"


class STYLE:
    DEFAULT = f"{COLOR.YELLOW}"
    DEBUG = f"{COLOR.BLUE}"
    DEBUG_TAG = f"{COLOR.BLACK}{COLOR.BG.YELLOW}"
    ERROR = f"{COLOR.RED}{COLOR.BG.BLACK}"
    ERROR_TAG = f"{COLOR.BLACK}{COLOR.BG.RED}"


