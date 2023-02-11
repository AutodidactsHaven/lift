"""
Incremental compilation requires the tracking of modified source files.
When a file has been changed, we can use this to compute what recompilation is required.

A cache is comprised of a relative path from the root project directory, and a last modified timestamp
stored in a comma seperated list, with one file per line.

E.g.

<filepath>, timestamp
"""

import os
import pathlib
import re
import lift.print_color as Out

class FileModifiedCache:
    parse_re = re.compile(r'"(.*)",(.*)')

    def __init__(self):
        self.cached_files = []      # list of src files we're caching mtimes of
        self.mtime_cache = {}       # lookup table of file -> mtime

    """Persist self.cached_files to disk"""
    def store(self):
        cache_dir = os.getcwd() + "/build/.cache/"

        # make directory if not already exists
        pathlib.Path(cache_dir).mkdir(parents=True, exist_ok=True) 

        with open(cache_dir + "file_mtimes", "w") as cache_file:
            for filepath in self.cached_files:
                file_mtime = os.path.getmtime(filepath)
                # save to <project_root>/build/.cache/file_mtimes
                cache_file.write(f'"{filepath}",{file_mtime}\n')

    def load(self):
        cache_dir = os.getcwd() + "/build/.cache/"
        # load from <project_root>/build/.cache/file_mtimes
        with open(cache_dir + "file_mtimes", "r") as cache_file:
            line = cache_file.readline()
            while line:
                filepath, mtime = self._parse_line(line)
                if not (filepath and mtime):
                    Out.print_error("Error parsing mtime file cache. Try running lift clean")
                    exit(1)

                self.cached_files.append(filepath)
                self.mtime_cache[filepath] = mtime

                line = cache_file.readline()

    def clear(self):
        self.cached_files = []
        self.mtime_cache = {}

    def _parse_line(self, line):
        match = self.parse_re.search(line)
        if match:
            return match.group(1), match.group(2)
        
        return None, None