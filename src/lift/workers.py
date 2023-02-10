import lift.print_color as Out

import os
import subprocess
import shlex
from threading import Thread
import time

class Workers:
    def internal_worker_capture(self, app, command):
        output, error = self.internal_worker_exe(app, command)
        if output:
            Out.print_normal(output)
        if error:
            Out.print_error(error)

    def internal_worker_exe(self, app, args_str):
        args = shlex.split(args_str)
        result = subprocess.run([app] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr

    threads = []
    def work(self, app, jobs_list):
        Out.print_info(f"> - Total {len(jobs_list)} jobs")
        for job in jobs_list:
            t = Thread(target=self.internal_worker_capture, args=(app, job))
            self.threads.append(t)
            t.start()

        Out.print_info("> - Waiting on all jobs to be done")
        done = 0
        for t in self.threads:
            t.join()
            done += 1
            Out.print_info(f"> - Done {done}/{len(jobs_list)}")
        Out.print_info("> - All workers are done")
