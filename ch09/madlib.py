#! python3

# madlib.py - Reads text files and lets the user add their own text wherever ADJECTIVE, NOUN, ADVERB, or VERB appears in the file
# For example: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.

from pathlib import Path
import re

# creates a formatted string of anything the regex should accpept
word_types = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']
regex = "|".join(word_types)

print('\n====== MAD LIBS ======\n')

# open file with read PLUS to allow reading and writing
madlib = Path('madlib.txt').read_text()

# print whole file (for user reference)
print(madlib + '\n')

# creates a list of found regexes
found_regex = re.findall(regex, madlib)

# if match, then replace
for word in range(len(found_regex)):
    madlib = re.sub(regex, input(f'Enter a new {found_regex[word].lower()}: '), madlib, 1)

# print updated mad lib
print(madlib)
