########################
# Author: Minghao Zhao
# Date: 4-15-2023
########################

 # This file contains a helper method to parse all of the md configuration file

def detect(path):
    file1 = open(path, "r")
    result = {}
    temp_control = []
    listFile = [line.rstrip() for line in file1]
    lineNum = 0
    while lineNum < len(listFile):
        i = 0
        while i < len(listFile[lineNum]):
            word = ''
            while (i < len(listFile[lineNum]) and (listFile[lineNum][i].isalnum() or listFile[lineNum][i] == '_')):
                word += listFile[lineNum][i]
                i+=1
            if i < len(listFile[lineNum]) and listFile[lineNum][i] == ' ':
                while listFile[lineNum][i] ==' ':
                    i+=1
            if i < len(listFile[lineNum]) and listFile[lineNum][i] == '=':
                i+=1
                while listFile[lineNum][i] == ' ':
                    i+= 1
                if listFile[lineNum][i] == "'":
                    temp = "'"
                    i+= 1
                    while listFile[lineNum][i] != "'":
                        temp+= listFile[lineNum][i]
                        i+=1
                    temp += "'"
                    result[word] = temp
                else:
                    temp = ''
                    while (i < len(listFile[lineNum]) and (listFile[lineNum][i].isalnum() or listFile[lineNum][i] == '_' or listFile[lineNum][i] =='.' or listFile[lineNum][i] == '-' or listFile[lineNum][i] == '/')):
                        temp += listFile[lineNum][i]
                        i+=1
                    result[word] = temp
            elif i < len(listFile[lineNum]) and listFile[lineNum][i].isalnum():
                continue
            else :
                if i < len(listFile[lineNum]) and  listFile[lineNum][i] =='&':
                    listresult = {}
                    if listFile[lineNum][i+1] == 'w' and listFile[lineNum][i+2] =='t':
                        if 'END' not in listFile[lineNum+1]:
                            while listFile[lineNum][1] != '/':
                                lineNum+=1
                                curi = 0
                                while curi < len(listFile[lineNum]):
                                    word = ''
                                    while (listFile[lineNum][curi].isalnum() or listFile[lineNum][curi] == '_'):
                                        word += listFile[lineNum][curi]
                                        curi+=1
                                    if listFile[lineNum][curi] == ' ':
                                        while listFile[lineNum][curi] ==' ':
                                            curi+=1
                                    if listFile[lineNum][curi] == '=':
                                        curi+=1
                                        while listFile[lineNum][curi] == ' ':
                                            curi+= 1
                                        if listFile[lineNum][curi] == "'":
                                            temp = "'"
                                            curi+= 1
                                            while listFile[lineNum][curi] != "'":
                                                temp+= listFile[lineNum][curi]
                                                curi+=1
                                            temp += "'"
                                            listresult[word] = temp
                                        else:
                                            temp = ''
                                            while (listFile[lineNum][curi].isalnum() or listFile[lineNum][curi] == '_' or listFile[lineNum][curi] =='.' or listFile[lineNum][curi] == '-' or listFile[lineNum][curi] == '/'):
                                                temp += listFile[lineNum][curi]
                                                curi+=1
                                            listresult[word] = temp
                                    elif listFile[lineNum][curi].isalnum():
                                        continue
                                    else:
                                        curi+=1
                    if len(listresult) != 0:
                        temp_control.append(listresult)
                i+= 1 
        lineNum+=1
    if len(temp_control) > 0:
        result['temp_control'] = temp_control
    return(result)


