import lift.print as out
from lift.files import FILES
from lift.compiler import COMPILER
from lift.color import COLOR

import os
import subprocess
import shlex
from threading import Thread
import time

def worker(command):
    output, error = run_compiler(command)
    if output:
        out.print_info(output)
    if error:
        print(error)

def run_compiler(args_str):
    args = shlex.split(args_str)
    result = subprocess.run(["clang"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr

def build(build_mode):
    out.print_info("Building the application");
    # Figure out which files we need to build
        # find all source files
        # find all .o files
        # compare timestamps
    # Build dependency graph for files we need to build
    # Generate compiler commands for making .o files
    # Feed compiler commands into threading system
    # Link .o into executable

    working_dir = os.getcwd()

    src_files = FILES("src") # TODO: Change to SRC, then change to lift_bulid.py var
    c_files = src_files.get_files_with_exensions({".c"});

    o_files = FILES("build")    

    # FIXME: For now we assume that all .c files need to be recompiles
    # timestamp checking should help with that, but need to be overwritten by
    # dependency graph when needed (.h was updated, all associated .c need to be rebuilt)

    if build_mode == COMPILER.DEBUG:
        flags = COMPILER(COMPILER.CLANG).generate_flags(COMPILER.DEBUG)
    else:
        flags = COMPILER(COMPILER.CLANG).generate_flags(COMPILER.RELEASE)

    threads = []
    out.print_info(f"Genereting .o for: {c_files}")
    out.print_info(f"Spawning {len(c_files)} workers")
    for c_file in c_files:
        o_file_name = c_file
        if "/" in c_file:
            o_file_name = c_file.split("/")[-1].replace(".c", ".o")
        command = f"{flags} -c '{working_dir}/{c_file}' -o '{working_dir}/build/{o_file_name}'"
        print(command) 
        t = Thread(target=worker, args=[command])
        threads.append(t)
        t.start()

    out.print_info("Waiting on all workers")
    done = 0
    for t in threads:
        t.join()
        done += 1
        out.print_info(f"Done {done}/{len(c_files)}")
    out.print_info("All workers are done")

    out.print_info("Linking .o's into executable")
    command = f"{flags} -o 'app' "
    o_files = FILES("build").get_files_with_exensions({".o"})
    if o_files:
        for file in o_files:
            command += f" '{working_dir}/{file}' "
    print(command)
    output, error = run_compiler(command)
    if output:
        out.print_info(output)
    if error:
        print(error)

    out.print_info("./app was generated!")
    out.print_info("Done")


def run():
    out.print_info("Running the application")
