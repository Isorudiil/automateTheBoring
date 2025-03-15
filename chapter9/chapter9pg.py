import os

totalSize = 0
for filename in os.listdir('/Users/katieherald'):
    totalSize += os.path.getsize(os.path.join('/Users/katieherald', filename))
print(totalSize)