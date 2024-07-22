from helpers.constant_helpers.simulation_constant_helper import *
from helpers.constant_helpers.directories_constant_helper import *
from pathlib import Path
import os
import time
import re
import random
import sys


def clear_all():
    clear_directory(MOVEMENT_DIR)
    clear_directory(PLOT_DIR)

def load_files_from_directory(path, file_format=".csv", n_sort=False):
    # import folder sa csvomima
    if not os.listdir(path):
        sys.exit("Directory is empty")

    files_dict = {}

    for r, d, f in os.walk(path):
        if n_sort:
            f = natural_sort(f)
        for file in f:
            if file_format in file:
                files_dict.update({file: os.path.join(r, file)})

    return files_dict

def natural_sort(l):
    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split("([0-9]+)", key)]

    return sorted(l, key=alphanum_key)

def clear_directory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files in {} deleted successfully." .format(directory_path))
    except OSError:
        print("Error occurred while deleting files. Try closing all files first.")

def get_current_time():
    current_time = time.strftime('%Y-%m-%d--%H-%M-%S')
    
    return current_time

def get_random_element_from_list(list):
    return random.choice(list)