#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ckkw : check out unknown katakana from specified file
#        unknown word willbe stored to unknown.txt
#        which will be merged into kkw.txt as a new word

import re
import sys
unknownkkw = []

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
        setnkkkw = set(unknownkkw)   # create uniq set
        unknownkkw = sorted(setnkkkw)   # sort it
        path = os.environ.get('UNKNOWNKKW', 'unknown.txt')
        with open(path, 'a') as unkf:
            unkf.write('\n'.join(unknownkkw))  # file unknow words with newline
            unkf.write('\n')


def ckline(lineno, line):
    klist = rekata.findall(line)
    if (len(klist) > 0):
        for w in klist:
            if not ckkw(w):
                print(lineno, line, end='')
                print("**", w, " is unknown")


def main():
    args = sys.argv
    if len(args) <= 1:
        print("Please specify filename")
        sys.exit(-1)
    initkkw()
    lineno = 0
    with open(sys.argv[1], 'r') as f:
        for line in f:
            lineno = lineno + 1
            ckline(lineno, line)
    finalizekkw()
    exit(0)


if __name__ == "__main__":
    main()
