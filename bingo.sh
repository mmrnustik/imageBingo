#!/bin/sh
# Usage:
# ./bingo.sh img_dir
# img_dir - directory with images from which do you want create bingo files

rm -r img
rm -r out
mkdir img
mkdir out

n=5    # side of bingo tile
count=80  # count of bingo tiles in result pdf
imgs='img'  # directory for storing converted images
s=256  # size of images

for i in `ls $1`; do convert $1/$i -resize $s"x"$s -gravity center -extent $s"x"$s $imgs/$i; done;

python2 bingo.py $n $count $imgs
python2 create_pdf.py


