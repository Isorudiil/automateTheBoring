#! python3
# fileSize.py - walks through a folder tree and searches for files larger than 100MB
# prints their absolute path to screen

import os
from pathlib import Path

path = Path(input('Enter the absolute path of the folder you would like to check:\n'))
sizeCheck = int(input('Find files larger than (value in MB):\n'))

for folderName, subfolders, filenames in os.walk(path):
    for file in filenames:
        folderPath = Path(folderName)
        filesize = os.path.getsize(folderPath / file)
        if filesize / (10**6) > sizeCheck:
            print(folderPath / file)
