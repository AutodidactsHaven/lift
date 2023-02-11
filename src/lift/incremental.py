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
import lift.helpers as helpers

class FileModifiedCache:
    def __init__(self):
        self.cached_files = []

    """Persist self.cached_files to disk"""
    def store(self):
        cache_dir = os.getcwd() + "/build/.cache/"

        # make directory if not already exists
        pathlib.Path(cache_dir).mkdir(parents=True, exist_ok=True) 

        f = open(cache_dir + "file_mtimes", "w")
        for filepath in self.cached_files:
            file_mtime = os.path.getmtime(filepath)
            # save to 'lift_build_path/build/.cache/file_mtimes
            f.write(f'"{filepath}",{file_mtime}\n')

        f.close()

    def load(self):
        # load from 'lift_build_path/build/.cache/file_mtimes
        # for line in ^file
        #   parse line -> push into self.cached_files
        pass
