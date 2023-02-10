import lift.print_color as Out

from threading import Thread
import time

def worker(command):
    output, error = worker_run(command)
    if output:
        Out.print_normal(output)
    if error:
        Out.print_error(error)

def worker_run(app, args_str):
    args = shlex.split(args_str)
    result = subprocess.run([app] + [args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout, result.stderr
