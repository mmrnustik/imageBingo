#!/bin/sh
rm -r img
rm -r out
mkdir img
mkdir out

s=256  # size of images

for i in `ls $1`; do convert $1/$i -resize $s"x"$s -gravity center -extent $s"x"$s img/$i; done;

python2 bingo.py
python2 create_pdf.py


