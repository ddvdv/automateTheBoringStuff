#! python3
# backupZi - Copies an entire folder and its content into a Zip file whose filename increments

import shutil, os, re

def pdfExtractor(folder):
    # Backup entire content of the 'folder' into a zip file.
    folder = os.path.abspath(folder) # make sure folder is absolute

    # create folder to received searched filed 
    if not os.path.exists('extractedFiles'):
        os.makedirs('extractedFiles')


    # regex replacing / by _
    strucRegex = re.compile('/')
    #numbering of the files
    fileNum = 1

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            oldNamePath = os.path.join(foldername, filename)
            structuredName = strucRegex.sub(' -> ', oldNamePath)
            numbName = str(fileNum) + structuredName
            print(numbName)
            newNamePath = os.path.join('.', 'extractedFiles', numbName)
            shutil.copy(oldNamePath, newNamePath)
            fileNum = fileNum + 1

    print('Done')

pdfExtractor('python')
