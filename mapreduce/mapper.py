#!/usr/bin/python
# The Mapper
import sys
import csv


iteration = 0
currentCountry = None
previousCountry = None
currentFx = None
previousFx = None
percentChange = None
currentKey = None
fxMap = []


if len(sys.argv) > 1:
    infile = open(sys.argv[1], "r")
else:
    infile = sys.stdin

next(infile)  
for line in infile:
    line = line.strip()
    
    line = line.split(',')
    try:

        currentCountry = line[0].rstrip()
        # print(currentCountry)
        red= line[3].rstrip()
        green= line[4].rstrip()
        blue=line[5].rstrip()
        currentKey=currentCountry+ " ("+red+" , "+green+" , "+blue+ ")"
        fxMap.append(tuple([currentKey,1]))


        previousCountry = currentCountry
        previousFx = currentFx
        previousLine = line


    except Exception as e:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(e).__name__, e.args)
        print("currentFx: %.2f previousFx: %.2f" % (currentFx, previousFx))
        print(message)
        sys.exit(0)

for i in sorted(fxMap):
    print("%-20s - %d" % (i[0], i[1]))
