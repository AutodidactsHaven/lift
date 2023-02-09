import os
import re

class FileNode:
    def __init__(self, absolute_path, filename):
        self.absolute_path = absolute_path
        self.filename = filename
        
    def __repr__(self) -> str:
        return f'{self.absolute_path}'

class DependencyGraph:
    def __init__(self):
        self.num_of_nodes = 0
        self.name_to_node_map = {}
        self.graph = {}

    def add_nodes(self, nodes):
        for node in nodes:
            self.name_to_node_map[node.filename] = node
            self.graph[node] = set()

    """if directional is true then node1 DEPENDS ON node2 but not other way around"""
    def add_dependency(self, node1, node2, directional=False):
        self.graph[node1].add(node2)

        if not directional:
            self.graph[node2].add(node1)

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

    def __str__(self) -> str:
        print_string = "Dependency Graph:\n"
        for node in self.graph:
            print_string += f'  {node.absolute_path} depends on [{self.graph[node]}]\n'
        return print_string

def extract_includes(text):
    # the regular expression pattern to match "#include"
    pattern = re.compile(r'#include\s+[<"](.*?)[>"]')

    # find all matches in the input text
    matches = re.findall(pattern, text)

    # return the list of matches
    return matches

if __name__ == "__main__":
    from files import FILES

    header_files = FILES("sample").get_files_with_exensions({".h"})
    header_file_nodes = [ FileNode(p, os.path.basename(p)) for p in header_files]

    source_files = FILES("sample").get_files_with_exensions({".c"})
    source_file_nodes = [ FileNode(p, os.path.basename(p)) for p in source_files]

    dgraph = DependencyGraph()
    dgraph.add_nodes(header_file_nodes)
    dgraph.add_nodes(source_file_nodes)

    # Let's deal with header files first
    for file in header_file_nodes:
        print("Handling ", file.absolute_path, file.filename)
        # parse file for #include s
        f = open(file.absolute_path, "r")
        file_contents = f.read()
        includes = extract_includes(file_contents)

        # for each include add_dependency
        for include in includes:
            target_node = dgraph.get_node_by_filename(include)
            if target_node:
                dgraph.add_dependency(file, target_node, directional=False) # header file includes are bidirectional
            else:
                print("couldnt find %s", target_node)

    # I know this could be done in one for loop but for now let's just be dumb :)        
    for file in source_file_nodes:
        print("Handling ", file.absolute_path, file.filename)
        f = open(file.absolute_path, "r")
        file_contents = f.read()
        includes = extract_includes(file_contents)
        print(includes)

        # for each include add_dependency
        for include in includes:
            target_node = dgraph.get_node_by_filename(include) or dgraph.get_node_by_absolute_path(include)
            print(target_node)
            if target_node:
                dgraph.add_dependency(file, target_node, directional=True) # source files rely on the header but not the other way around
            else:
                print("couldnt find ", target_node)

    print(dgraph)
            