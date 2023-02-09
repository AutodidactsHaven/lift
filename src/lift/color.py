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
