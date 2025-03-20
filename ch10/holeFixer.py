#! python3
# holeFixer.py - fixes a hole found in file numbers, also implements spamGen module
# in case you don't have any numbered files.

import os
from pathlib import Path as P
import re as r
import spamGen as sG
import time as t


spamCheck = input('Would you like spam generated (yes or no)?\n').lower()

if spamCheck == 'yes':
    path = P(input('Where would you like to generate spam?\n'))
    numFiles = int(input('How many spam files would you like?\n'))
    nameFile = input('What would you like your spam to be called?\n')
    sG.generator(path, numFiles, nameFile)
else:
    path = P(input('What directory holds your missing file?\n'))
    nameFile= input('What is the common name of your files?\n')
    
regex = r.compile(f'({nameFile})(\\d*)(.*)')

print('Are you ready to find the hole?')
t.sleep(2)
holeCheck = input('Did you have time to find the hole?\n').lower()

if holeCheck == 'yes':
    for folderName, subfolders, filenames in os.walk(path):
        num = 0;
        for file in filenames:
            fileRegexMatch = regex.search(file)
            if fileRegexMatch == None:
                continue
            if fileRegexMatch.group(2) == str(num).zfill(3):
                num += 1
            else:
                newFile = open(path / f'{nameFile}{str(num).zfill(3)}.txt', 'a')
                newFile.write('this is spam!')
                newFile.close()
                num += 1