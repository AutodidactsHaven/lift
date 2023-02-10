# lift

Some intended features:

- Installable CLI via `pip`
- Extensible via Python
- Zero configuration project init and sample build file


# CLI Commands

`lift init` - generates `lift_build.py` in the root folder with the default parameters

`lift build` - Generates the build in a debug mode

`lift build release/debug` - Generates the build in a spicified mode

`lift run` - Generates the build and runs the app in the debug mode

`lift run release/debug` - Generates the build in a spicified mode and runs the app

`lift test` - Runs unit tests

`lift clean` - Removes everything from build directory

Not implemented `lift add raysan5/raylib` - Creates _deps directory in project root and pulls from github & Make the module 

# .lift.conf

User can overwrite default parameters used by `lift init` through creation of `.lift.conf` in one of the ENV paths.

# How to build & run

0) Install setuptools `pip install setuptools`

1) Remove old build `rm -r dist`

2) Build `python setup.py sdist`

3) Uninstall old version if version number changed `yes | pip uninstall lift`

4) Install `pip install dist/lift*.gz`

5) Run `lift`

**OR**

0) Install setuptools `pip install setuptools`

1) Run `./build.sh`

2) Run `lift`
