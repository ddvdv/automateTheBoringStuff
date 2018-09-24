#! python3
# backupZi - Copies an entire folder and its content into a Zip file whose filename increments

import zipfile, os

def backupToZip(folder):
    # Backup entire content of the 'folder' into a zip file.
    folder = os.path.abspath(folder) # make sure folder is absolute

    # figure out the filename this code should use base on what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
          break
        number = number + 1

    # Create the Zip file
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print("Adding files in %s... " % (foldername))
        # Add the current folder to the ZIP file.
        #backupZip.write(foldername)
        # Add all the files in this folder to the Zip file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # don't back up the zip files
            elif filename.endswith('.pdf'):
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')

backupToZip('python')
