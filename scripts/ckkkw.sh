#!/bin/bash
# ckkkw.sh : integrated katakana checker
# Usage: ckkkw [URL|file.docx|file.pdf|file.txt]
WORKFILE=/tmp/ckkkw-$$.txt
if [ $# -gt 0 ]; then
  for i in $*
  do 
     if [ ${i:0:4} = "http" ]; then
        curl -s -k $i | html2text -utf8 >$WORKFILE
     elif [ ${i##*.} = "docx" ]; then
           docx2txt $i $WORKFILE
     elif [ ${i##*.} = "odt" ]; then
           odt2txt $i --output=$WORKFILE
     elif [ ${i##*.} = "pdf" ]; then
           pdftotext $i $WORKFILE
     else
           cp $i $WORKFILE
     fi
     ckkw $WORKFILE
  done
else
     cat  >$WORKFILE
     ckkw $WORKFILE
fi
