
# TODO: use a custom class for more metadata tracking?
class Node:
    def __init__(self):
        pass

class DependencyGraph:
    def __init__(self):
        self.num_of_nodes = 0
        self.graph = {}

    def add_files(self, filepaths):
        for filepath in filepaths:
            self.graph[filepath] = set()

    """if directional is true then node1 DEPENDS ON node2 but not other way around"""
    def add_dependency(self, node1, node2, directional=False):
        self.graph[node1].add(node2)

        if not directional:
            self.graph[node2].add(node1)

if __name__ == "__main__":
    from files import FILES
    files = FILES("sample").get_files_with_exensions({".h",".c"})
    print(files)
    dgraph = DependencyGraph().add_files(files)
    for file in files:
        print("Handling ", file)
        # 1. parse file for #include s
        # 2. resolve relative paths to absolute paths
        # 3. for each include:
        #       add_dependency(...)