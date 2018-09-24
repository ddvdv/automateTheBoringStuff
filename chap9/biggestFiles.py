#! python3
# list the biggest folders and files on the folder

import os

def calcSize(folder):
    # check if path is absolute
    folder = os.path.abspath(folder)

    for folder, subfolders, filenames in os.walk(folder):
        size = os.path.getsize(folder)
        if size > 50000:
            print(str(folder) + ' -> ' + str(os.path.getsize(folder)))

calcSize('.')
