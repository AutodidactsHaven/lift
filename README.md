# lift

Some intended features:

- Installable CLI via `pip`
- Extensible via Python
- Zero configuration project init and sample build file


# CLI Commands

`lift init` - generates `lift_build.py` in the root with default parameters

`lift debug build` - Generates ./build/debug

`lift debug run` - Generates ./build/debug and runs executable

`lift release build` - Generates ./build/release

`lift release run` - Generates ./build/release and runs executable

`lift test` - Runs unit tests

`lift clean` - Removes everything from build directory

`lift add raysan5/raylib` - Creates _deps directory in project root and pulls from github & Make the module 
