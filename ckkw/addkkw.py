#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# addwd: add words to kkw

import os
import sys

FNAME = 'kkw.txt'
FULLKKWPATH = os.environ.get('KKWPATH', '')


def loadkkw():
    # load existing kkw from KKWPATH/kkw.txt
    fullname = FULLKKWPATH + FNAME
    katabuf = [line.rstrip('\n') for line in open(fullname)]
    return katabuf


def storekkw(kkw, addwords):
    # store addwords into kkw
    import datetime

    TMPFNAME = FNAME.replace('.txt', '.tmp.txt')
    OLDFNAME = FULLKKWPATH + FNAME.replace('.txt', '.old.txt')

    # sort and remove duplicated words
    newkkw = kkw
    newkkw.extend(addwords)
    newkkw.sort()

    str = '\n'.join(newkkw)
    with open(TMPFNAME, 'wt') as f:
        f.write(str)
    print(len(addwords), " words stored")

    # 旧ファイルを +oldに rename し仮ファイルを正式に
    os.rename(FULLKKWPATH + FNAME, OLDFNAME)
    os.rename(TMPFNAME, FULLKKWPATH + FNAME)

    # log を出す
    now = datetime.datetime.now()
    LOGFILE = now.strftime("%Y%m%d")+'.log'
    LOGFILE = FULLKKWPATH + "Log-" + LOGFILE
    # print LOGFILE
    logf = open(LOGFILE, 'a')
    date = '%s' % (now)
    logf.writelines(date+'\n')
    logf.writelines('%s words added\n' % len(addwords))
    logf.writelines('total %s words\n' % len(newkkw))
    logf.close


def readaddwords(file):
    # read word to be update
    addw = [line.rstrip('\n') for line in open(file)]
    return set(addw)


import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="File name")
    parser.add_argument("-d", "--dryrun", action="store_true", 
                        help="Do not add kkw")
    args = parser.parse_args()
    addfile = args.filename

    kkwtbl = loadkkw()
    newwords = readaddwords(addfile)

    nkkw = []
    for w in newwords:
        if len(w) > 0 :
            # check w is in the db?
            if w not in kkwtbl:
                nkkw.append(w)
                print(w)
            else:
                print(w, " already exist")
    print(len(nkkw), " added to kkw")
    if not args.dryrun :
        storekkw(kkwtbl, nkkw)
    else:
        print ("Nothing updated because of dryrun")

if __name__ == "__main__":
    main()
    sys.exit(0)
