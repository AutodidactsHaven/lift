import os

def get_lift_build_path():
    working_dir = os.getcwd()
    lift_build_path = working_dir + "/lift_build.py"
    return lift_build_path