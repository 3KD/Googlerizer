#!/usr/bin/env python3

from googlesearch import *
import webbrowser

exec(open("./stripper.py").read())

chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
f=open("List.txt", "r")

f1 = f.readlines()

for i in f1:
    query = str(i)
    url = "https://www.google.com/search?q=" + str(i)
    webbrowser.get(chrome_path).open(url)
    
    
    