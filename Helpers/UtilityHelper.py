from Helpers.ConstantHelper import *
from pathlib import Path
import os
import time
import random


def clearAll():
    clearDirectory(getOutputDirectory())
    clearDirectory(getAnimationDirectory())
    clearDirectory(getPlotDirectory())

def getOutputDirectory():
    path = Path(os.getcwd())

    return str(path) + "/Output"

def getInputDirectory():
    path = Path(os.getcwd())

    return str(path) + "/Input"

def getAnimationDirectory():
    path = Path(os.getcwd())

    return str(path) + "/Visualization/Animation"

def getPlotDirectory():
    path = Path(os.getcwd())

    return str(path) + "/Visualization/Static"

def clearDirectory(directory_path):
    try:
        files = os.listdir(directory_path)
        for file in files:
            file_path = os.path.join(directory_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        print("All files in {} deleted successfully." .format(directory_path))
    except OSError:
        print("Error occurred while deleting files. Try closing all files first.")

def getCurrentTime():
    current_time = time.strftime('%Y-%m-%d--%H-%M-%S')
    
    return current_time

def getRandomElementFromList(list):
    return random.choice(list)