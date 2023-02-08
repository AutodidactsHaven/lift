# lift

Some intended features:

- Installable CLI via `pip`
- Extensible via Python
- Zero configuration project init and sample build file


# CLI Commands

`lift init` - generates `lift_build.py` in the root with default parameters

Generates ./build/debug
`lift debug build`
Generates ./build/debug and runs executable
`lift debug run`

Generates ./build/release
`lift release build`
Generates ./build/release and runs executable
`lift release run`

Runs unit tests
`lift test`

Removes everything from build directory
`lift clean`

Creates _deps directory in project root and pulls from github & Make the module 
`lift add raysan5/raylib`
