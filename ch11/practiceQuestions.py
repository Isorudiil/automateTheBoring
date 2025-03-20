# 1.
spam = 0
assert spam >= 10

# 2.
eggs = 'hello'
bacon = 'Hello'
assert eggs.lower() != bacon.lower()

# 3.
# assert False

# 4.
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 5.
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 6.
logging.DEBUG
logging.INFO
logging.WARNING
logging.ERROR
logging.CRITICAL

# 7.
logging.disable(logging.CRITICAL)

# 8.
# you can disable logging, or print the debug info to a txt file

# 9.
# step over:
#   will skip function call
# step in:
#   it will step into a function call
# step out:
#   if you're in a function call, it will continue until the function call is complete

# 10.
# once the program has completed running

# 11.
# a place in your program to stop execution and begin steps

# 12.
# by clicking the line number