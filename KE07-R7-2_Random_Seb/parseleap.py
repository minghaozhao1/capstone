########################
# Author: Minghao Zhao
# Date: 4-15-2023
########################

# This file contains a helper method to parse the leap.in file

import re

def parseleap(newfilepath):
    file1 = open(newfilepath, "r")
    result = {}
    temp_control = []
    mdParameter = []
    issolvated = False
    solvatebox = []
    listFile = [line.rstrip() for line in file1]
    lineNum = 0
    while lineNum < len(listFile):
        if 'source' in listFile[lineNum]:
            i = 0
            match = re.search('source leaprc', listFile[lineNum])
            res = listFile[lineNum][match.end()+1:]
            mdParameter.append(res)
        if re.search("solvate(\w+) +.+? +([\w\d]+) +(\d+)", listFile[lineNum]):
            issolvated=True
            solvatebox= [x for x in re.match("solvate(\w+) +.+? +([\w\d]+) +(\d+)", listFile[lineNum]).groups()]
        lineNum+=1
    result = {'issolvated': issolvated,
            'solvatebox': solvatebox,
            'mdparameter': mdParameter}
    return result
