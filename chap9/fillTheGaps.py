#! python3
# find the numbered files and locates and gaps in the numbering

import os, shutil, re

def checkNumbering(folder):
    folder = os.path.abspath(folder)

    number = 1
    startNumbReg = re.compile(r'^\d\d\d')

    for folder, subfolders, files in os.walk(folder):
        for file in files:
            result = startNumbReg.search(file)
            if result is not None and result.group() is not '':
                print(file)
                number = number + 1
            if number > 100:
                break

checkNumbering('.')
