import lift.print_color as out

# Flags for GCC / Clang
class COMPILER:
    def __init__(self, which_compiler):
        self.CURRENT_COMPILER = which_compiler

    GCC = "GCC"
    CLANG = "CLANG"
    ALL = "ALL"
    GCC_COLORS="export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'"
    RELEASE = "RELEASE"
    DEBUG = "DEBUG"
    HARDENED = "HARDENED"

    CURRENT_COMPILER = CLANG

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
        "-Wstack-protector": ALL,
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

    def generate_flags(self, compilation_mode):
        flags = ""
        if compilation_mode == self.DEBUG:
            for flag in self.flags_debug:
                if self.flags_debug[flag] == self.ALL or self.flags_debug[flag] == self.CURRENT_COMPILER:
                    flags += f" {flag}"
        elif compilation_mode == self.RELEASE:
            for flag in self.flags_release:
                if self.flags_release[flag] == self.ALL or self.flags_release[flag] == self.CURRENT_COMPILER:
                    flags += f" {flag} "
        elif compilation_mode == self.HARDENED:
            for flag in self.flags_hardened:
                if self.flags_hardened[flag] == self.ALL or self.flags_hardened[flag] == self.CURRENT_COMPILER:
                    flags += f" {flag}"
        else:
            out.print_error(f"{compilation_mode} is not a valid compilation mode")
        return flags;


