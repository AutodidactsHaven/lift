import os
import re

"""
Given the example layout in /sample we can create an include graph which looks something like this

  ---------         ---------
 | magic.c | ----> | magic.h | <--------|
  ---------         ---------           |
                        ^            --------
                        |           | main.c |
  ----------        ----------       --------
 | player.c | ---> | player.h | <-------|
  ----------        ----------

It is a dependency graph such that we can ascertain *which* c files must be recompiled when a particular .h file has been
modified by traversing the graph.

If a '.c' source file has been modified, then only itself is recompiled
If a '.h' header file has been modified, the graph must be walked to find all header files that include that header file
                                         either directly or via another include. any '.c' source files that depend on any
                                         of those header files must be recompiled
E.g.

If player.c is modified, only player.o must be recompiled
If magic.c is modified, only magic.o must be recompiled
if main.c is modified, only main.o must be recompiled
If player.h is modified, player.o and main.o must be recompiled 
Finally, if magic.h is modified, magic.o, player.o, and main.o all must be recompiled.
This is because player.h #includes magic.h, meaning a change to magic.h will modify the contents of player.h after the preprocessor has run.
Any source file depending on player.h must therefore also be recompiled.
"""

class FileNode:
    def __init__(self, absolute_path, filename):
        self.absolute_path = absolute_path
        self.filename = filename
        
    def __str__(self) -> str:
        return self.absolute_path

    def __repr__(self) -> str:
        return f'{self.filename}'

class DependencyGraph:
    def __init__(self):
        self.num_of_nodes = 0
        self.name_to_node_map = {}
        self.graph = {}

    def add_nodes(self, nodes):
        for node in nodes:
            self.name_to_node_map[node.filename] = node
            self.graph[node] = set()

    """ node2 depends on node1 """
    def add_dependency(self, node1, node2, directional=False):
        self.graph[node2].add(node1)

        if not directional:
            self.graph[node1].add(node2)

    def get_node_by_filename(self, filename):
        if self.name_to_node_map.get(filename):
            return self.name_to_node_map[filename]
        else:
            return None
    
    def get_node_by_absolute_path(self, p):
        for node in self.graph:
            if node.absolute_path == p:
                return node
        return None

    """returns all children .c files that depend on start_node"""
    def accumulate_dependencies(self, start_node):
        visited = {}
        deps = self._accumulate_dependencies(start_node, visited)
        return deps

    def _accumulate_dependencies(self, node, visited):
        deps = []
        for dependent in self.graph[node]:
            # print(f'{node.filename} > {dependent.filename}')
            absolute_path = dependent.absolute_path
            if absolute_path not in visited:
                visited[absolute_path] = True
                child_deps = self._accumulate_dependencies(dependent, visited)
                for d in child_deps:
                    deps.append(d)
            # else already accounted for

            if absolute_path.endswith('.c'):
                deps.append(absolute_path)

        return deps

    def __str__(self) -> str:
        print_string = "Dependency Graph:\n"
        for node in self.graph:
            print_string += f'  {node.absolute_path} has these dependents [{self.graph[node]}]\n'
        return print_string