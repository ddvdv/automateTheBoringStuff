#! python3
# Browse through all files of the directory (tree style), and look for a provided regex inside .txt files

import re, os

regUser = input("What regex are you looking for ?") or 'EEE'
regObj = re.compile(regUser)
print(regObj)

pathFile = os.path.abspath('regFuel.txt')

searchFile = open(pathFile, 'r')
regResult = regObj.search(searchFile.read())
print('Number of hint: ' + str(len(regResult.group())))
print(regResult.group())
searchFile.close()
