#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ckkw : check out unknown katakana from specified file
#        with create unknown.txt as list of onknonw word to be merged into kkw.txt

unknownkkw=[]
import re
# カタカナの　テストーデスよ オープン : this is a sample text for setlf input
pattern = u'[\u30a1-\u30fa\u30fc]+'  # カタカナ
rekata = re.compile(pattern)

def initkkw():
    import os
    # initialize for ckkw
    # read kkw.txt and into kkw list
    # Engironent file KKWFILE is the place of kkw.txt
    global kkw
    Defaultkkwf = 'kkw.txt'
    kkwpath = os.environ.get('KKWPATH', '')
    kkwfile = kkwpath + Defaultkkwf
    with open(kkwfile) as kkwf:
        kkw = kkwf.read().splitlines()
    #print ("kkw read completed", len(kkw))

def ckkw(word):
    # check word is on the kkw list and return ture if exist
    global kkw, unknownkkw
    if not (word in kkw):
        unknownkkw.append(word)  # collect unknown word
    return word in kkw

def finalizekkw():
    import os
    global unknownkkw
    if (len(unknownkkw) > 0):
        unknownkkw = set(unknownkkw)
        #print (unknownkkw)
        path = os.environ.get('UNKNOWNKKW', 'unknown.txt')
        with open(path, 'a') as unkf:
            unkf.write('\n'.join(unknownkkw))  # file inknow words with newline

def ckline(lineno, line):
    klist = rekata.findall(line)
    if (len(klist) > 0):
        #print (line, end='')
        #print (klist)
        for w in klist:
            if not ckkw(w) :
                print (lineno, line, end='')
                print ("**", w, " is unknown")

import sys
def main():
    args = sys.argv
    if len(args) <= 1:
        print ("Please specify filename")
        sys.exit(-1)
    initkkw()
    lineno = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            #print (line, end="")
            lineno = lineno + 1
            ckline(lineno, line)
    finalizekkw()
    exit (0)

if __name__ == "__main__":
    main()
