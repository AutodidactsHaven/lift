import os

# Use example:
# files = FILES("sample")
# lift_print(files.all_files)
# lift_print(files.get_files_with_exensions({".h",".c"}));
class Files:
    all_files = []
    def __init__(self, directory):
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.all_files = self.internal_get_all_files(directory)
        
    def internal_get_all_files(self, directory):
        file_paths = []
        for root, directories, files in os.walk(directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    # use: files.get_files_with_exensions({".h", ".c"}) -> {"src/item1.c", "src/headers/item1.h")
    def get_files_with_exensions(self, extensions):
        files = []
        for file in self.all_files:
            for extension in extensions:
                if file.endswith(extension):
                    files.append(file)
        return files
