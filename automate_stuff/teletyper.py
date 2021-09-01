# redandgreen.co.uk #
# put your code in a file called scores.txt 

import time
import sys
import random

inp_file = "scores.txt"

def teletype_print(text):
    for ch in text:
        print(ch, end="")
        time.sleep(random.random() * 0.5)
        #sys.stdout.flush()
        #sys.stdout.write()
        with open ("vcode.py", "a") as pyf:
            pyf.write(ch)
        
    #print("\n")

def fetch_scores(inp_file):
    with open (inp_file,"r") as inpf:
        teletype_print(inpf.read())


fetch_scores(inp_file)

