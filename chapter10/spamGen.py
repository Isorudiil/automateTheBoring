#! python3
# spamGen.py - Ever wanted to generate a bunch of useless files to use
# for practice coding problems? Look no further than spamGen.
# spamGen will generate your provided prefix appended with numbers at the
# end so you can test certain programs. It will even add in a random
# missing file!

from pathlib import Path as p
import random as r

def generator(path, numFiles, nameFile):
    missingFile = r.randint(0, numFiles)
    for number in range(numFiles):
        if number == missingFile:
            continue
        file = open(path / f'{nameFile}{str(number).zfill(3)}.txt', 'a')
        file.write('this is spam!')
        file.close()


if __name__ == "__main__":
    path = p(input('Where would you like your spam files?\n'))
    numFiles = int(input('How many spam files would you like?\n'))
    nameFile = input('What would you like your spam to be called?\n')
    generator(path, numFiles, nameFile)