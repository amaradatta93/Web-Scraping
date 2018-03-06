import os


def create_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory" + directory)
        os.makedirs(directory)
