import os;

# Flags for GCC / Clang
class COMPILER:

    GCC = "GCC"
    CLANG = "CLANG"
    ALL = "ALL"
    GCC_COLORS="export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'"

    flags_debug = {
        "-g": ALL,
        "-Wall": ALL,
        "-fsanitize=address,undefined": ALL,
        "-Wall": ALL,
        "-Wextra": ALL,
        "-fno-omit-frame-pointer": ALL,
        "-Wshadow": ALL,
        "-Wnull-dereference": ALL,
        "-Wcast-qual": ALL,
        "-Wformat-security": ALL,
        "-stack-protector": ALL,
        "-Warray-bounds": ALL,

        "-Wcast-align=strict": GCC,
        "-Wcast-align": CLANG,
        "-fcolor-diagnostics": CLANG,
        "-fdiagnostics-color=always": GCC,
        "-Warray-bounds-pointer-arithmetic": CLANG,
        "-Wassign-enum": CLANG,
    }

    flags_hardened = {
        "-fstack-protector": ALL,
    }

    flags_release = {
        "-O3": ALL,
    }

