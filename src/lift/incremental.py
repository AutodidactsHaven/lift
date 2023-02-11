"""
Incremental compilation requires the tracking of modified source files.
When a file has been changed, we can use this to compute what recompilation is required.

A cache is comprised of a relative path from the root project directory, and a last modified timestamp
stored in a comma seperated list, with one file per line.

E.g.

<filepath>, timestamp
"""

import lift.helpers as helpers

class FileModifiedCache:
    def __init__(self):
        self.cached_files = []

    """Persist self.cached_files to disk"""
    def store():
        lift_build_path = helpers.get_lift_build_path()
        # for file in self.cached_files
        #   save to 'lift_build_path/build/.cache/file_mtimes

    def load():
        # load from 'lift_build_path/build/.cache/file_mtimes
        # for line in ^file
        #   parse line -> push into self.cached_files