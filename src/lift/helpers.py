import os

def get_lift_build_path():
    working_dir = os.getcwd()
    lift_build_path = working_dir + "/lift_build.py"
    return lift_build_path

# TODO

def project_root_dir_path():
    pass

def build_dir_path():
    working_dir = os.getcwd()
    build_dir_path = working_dir + "/build/"
    return build_dir_path