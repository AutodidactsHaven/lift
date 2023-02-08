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

# .lift.conf

User can overwrite default parameters used by `lift init` through creation of `.lift.conf` in one of the ENV paths.

# How to build

0) Install setuptools `pip install setuptools`

1) Remove old build `rm -r dist`

2) Build `python setup.py sdist`

3) Uninstall old version if version number chan `yes | pip uninstall lift`

4) Install `pip install dist/lift*.gz`

5) Run `lift`

**OR**

0) Install setuptools `pip install setuptools`

1) Run `./build.sh`

2) Run `lift`
