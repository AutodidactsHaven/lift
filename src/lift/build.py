import lift.print_color as Out
import lift.lift_class import LiftClass

class Build:
    build_LiftClass = LiftClass()

    def build(self, arg_build_LiftClass):
        Out.print_debug(f"> Build.build() Compiling and linking")
        self.build_LiftClass = arg_build_LiftClass

        self.remove_old_executable()
        source_files = self.get_files_to_compile()
        self.compile(source_files)
        self.link()

    def compile(self):
        Out.print_debug(f"> Build.compile() Compiling")

    def link(self):
        Out.print_debug(f"> Build.link() Linking")

    def get_files_to_compile(self):
        Out.print_debug(f"> Build.get_files_to_compile()")

