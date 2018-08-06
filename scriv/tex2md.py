#!/usr/bin/env python

import os,sys

text=sys.stdin.read()

while True:
    try:
        idx1=text.index(r'{\em ')
        idx2=text[idx1:].index('}')
        text=text[:idx1]+"*"+text[(idx1+5):(idx1+idx2)]+"*"+text[(idx1+idx2+1):]
    except ValueError:
        break

while True:
    try:
        idx1=text.index(r'{\bf ')
        idx2=text[idx1:].index('}')
        text=text[:idx1]+"**"+text[(idx1+5):(idx1+idx2)]+"**"+text[(idx1+idx2+1):]
    except ValueError:
        break

while True:
    try:
        idx1=text.index(r'\emph{')
        idx2=text[idx1:].index('}')
        text=text[:idx1]+"*"+text[(idx1+6):(idx1+idx2)]+"*"+text[(idx1+idx2+1):]
    except ValueError:
        break

while True:
    try:
        idx1=text.index(r'\marginnote{')
        idx2=text[idx1:].index('}')
        text=text[:idx1]+"[^"+text[(idx1+12):(idx1+idx2)]+"]"+text[(idx1+idx2+1):]
    except ValueError:
        break


while True:
    try:
        idx1=text.index(r'\bi'+"\n")
        idx2=text[idx1:].index(r'\ei'+"\n")

        subtext=text[(idx1+4):(idx1+idx2)]
        subtext=subtext.replace(r"\i ","* ")

        text=text[:idx1]+subtext+text[(idx1+idx2+4):]
    except ValueError:
        break

while True:
    try:
        idx1=text.index(r'\be'+"\n")
        idx2=text[idx1:].index(r'\ee'+"\n")

        subtext=text[(idx1+4):(idx1+idx2)]
        subtext=subtext.replace(r"\i ","1. ")

        text=text[:idx1]+subtext+text[(idx1+idx2+4):]
    except ValueError:
        break

text=text.replace("``",'"')
text=text.replace("''",'"')
text=text.replace("<!--",'')
text=text.replace("-->",'')

print
print "======================="
print
print text

with open("out.txt","w") as fid:
    fid.write(text)

