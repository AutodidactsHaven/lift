
# - CLI COMMANDS
# init
# debug build
# release build
# debug run
# release run
# test
# clean
# add libname
class CLI:
    init= "init"
    debug= "debug"
    release= "release"
    test= "test"
    clean= "clean"
    add= "add"
    help= "help"
    build= "build"
    run= "run"

    actions = {
        "init": init,
        "debug": debug,
        "release": release,
        "test": test,
        "clean": clean,
        "add": add,
        "help": help
    }

    parameters = {
        "build": build,
        "run": run,
    }
