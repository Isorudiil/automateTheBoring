import os, re
from pathlib import Path

# extension = input('What extension would you like to copy (format: .jpg)? ')
# fileRegex = re.compile(f'.*?{extension}')
path = Path('C:\\automateTheBoring\\chapter10\\CAD Projects\\2024\\235013 - Ram Part Number Changes')

# for foundFile in os.listdir(path):
#     mo = fileRegex.search(foundFile)
#     if mo == None:
#         continue
#     print(mo.group())

for folderName, subfolders, filenames in os.walk(path):
    # print(folderName)
    # print(subfolders)
    # print(filenames)
    for file in filenames:
        print(f'{folderName}\{file}')