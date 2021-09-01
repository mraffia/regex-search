#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression

from pathlib import Path
import re

def regexSearch(regex):
    p = Path.cwd()
    allTextFiles = list(p.glob('*.txt'))  # Lists all text files from cwd

    userRegex = re.compile(regex)

    matches = []

    for i in range(len(allTextFiles)):
        textFile = open(str(allTextFiles[i]))
        for line in textFile.readlines():
            mo = userRegex.search(line)
            if mo != None:
                matches.append(line.rstrip() + ' - from ' + allTextFiles[i].name)

    for item in matches:
        print(item)

    return matches
