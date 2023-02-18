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
            Out.print_normal(error)

    def internal_worker_exe(self, app, args_str):
        args = shlex.split(args_str)
        result = subprocess.run([app] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout, result.stderr

    def work(self, app, jobs_list, thread_limit):
        threads = []
        Out.print_info(f"> - Total {len(jobs_list)} jobs")
        done = 0
        for job in jobs_list:
            if len(threads) >= thread_limit:
                for t in threads:
                    t.join()
                threads = []
            t = Thread(target=self.internal_worker_capture, args=(app, job))
            threads.append(t)
            t.start()
            done += 1
            Out.print_info(f"> - ↺  {done}/{len(jobs_list)} {int((done / len(jobs_list)) * 100 + 0.5)}%")

        for t in threads:
            t.join()
        Out.print_info("> - All jobs finished")
