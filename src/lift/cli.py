
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
    actions = {
        "init": "init",
        "debug": "debug",
        "release": "release",
        "test": "test",
        "clean": "clean",
        "add": "add"
    }

    parameters = {
        "build": "build",
        "run": "run",
    }
