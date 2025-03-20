#! python3
# selectiveCopy.py - walks through a folder tree and searches for files with
# a certain file extension (.pdf, .jpg, etc.). Copies these files from their
# current location to a specified new location.

# thoughts: use os.walk() to to through folder tree
# use shutil.move() to physically move the files
# use re.compile() for a regex to find correct extension

import os
import re
import shutil
from pathlib import Path

extension = input('What extension would you like to copy (format: .jpg, regexes accepted)?\n')
folder = Path(input('Please provide the absolute path to the folder you want to copy from:\n'))
newFolder = Path(input('Please input the absolute path to your new folder:\n'))

fileRegex = re.compile(f'.*?{extension}')

for folderName, subfolders, filenames in os.walk(folder):
    for file in filenames:
        foundFile = fileRegex.search(file)
        if foundFile == None:
            continue
        oldfolder = Path(folderName)
        shutil.copy(oldfolder / file, newFolder)