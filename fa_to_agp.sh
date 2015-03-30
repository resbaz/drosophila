#!/bin/bash

# This is a automated version of the steps listed here:
# http://genomewiki.ucsc.edu/index.php/Building_a_new_genome_database
# Note that edge cases haven't been tested strongly

# This script will convert a .fa file into something that can be loaded into 
# the enome browser database 

# usage: fa_to_agp.sh <fa-file> <output-name>
# eg: fa_to_agp.sh D_birchii.scafSeq.fill.v1.0.fa droBir1

# Note: this has not been tested against edge cases, and only against the 
# single supplied .fa file

echo "total $#"

if [ $# != 2 ]; then
    echo "Usage: $0 <fa-file> <output-name>";
    echo "";
    echo "eg: fa_to_agp.sh D_birchii.scafSeq.fill.v1.0.fa droBir1"
    echo "";
    echo "Not enough parameters"	    
    echo "";
    exit 1;
fi

if [ ! -f $1 ]; then
    echo "Usage: $0 <fa-file> <output-name>";
    echo "";
    echo "eg: fa_to_agp.sh D_birchii.scafSeq.fill.v1.0.fa droBir1"
    echo "";
    echo "First parameter isn't a file"	    
    echo "";
    exit 1;
fi 

FA_FILE="$1"   # eg D_birchii.scafSeq.fill.v1.0.fa
BASE_NAME="$2" # eg droBir1
AGP_FILE="$2".agp
TWO_BIT_FILE="$2".2bit

GB_SOURCE=/home/ubuntu/src/gb

echo ""

# Step 2

if [ ! -f $AGP_FILE ]; then
    echo "Creating the AGP file..."
    hgFakeAgp -minContigGap=1 $FA_FILE $AGP_FILE
fi

# Step 3 

if [ ! -f $TWO_BIT_FILE ]; then
    echo "Creating the 2bit file..."
    faToTwoBit $FA_FILE $TWO_BIT_FILE
else TB_EXISTS=1
fi

if [ ! -d /gbdb/$BASE_NAME ]; then
    echo "Creating folders for db..."
    mkdir /gbdb/$BASE_NAME
else echo "/gbdb/$BASE_NAME already exists"
fi
if [ ! -d /gbdb/$BASE_NAME/html ]; then
    echo "Creating folders for db..."
    mkdir /gbdb/$BASE_NAME/html
else echo "/gbdb/$BASE_NAME/html already exists"
fi

echo "Creating a symlink from local files to db folder structure..."

ln -s `pwd`/$TWO_BIT_FILE /gbdb/$BASE_NAME/$TWO_BIT_FILE

# Step 4

echo "Checking the agp and fa file are the same..." 
sleep 2

if [ ! $TB_EXISTS ]; then 
    checkAgpAndFa $AGP_FILE $FA_FILE
fi

# Step 5

echo ""
echo "Creating the chromInfo file..."

twoBitInfo $TWO_BIT_FILE stdout | sort -k2nr > chrom.sizes

if [[ ! -d bed ]] || [[ ! -d bed/chromInfo ]]; then
    echo "Creating chromInfo folder..."
    mkdir -p bed/chromInfo
fi

echo "Adding $1 to the end of the chromInfo.tab file..."

TW_PATH=/gbdb/$BASE_NAME/$TWO_BIT_FILE

echo $TW_PATH | awk -v VAR=${TW_PATH} '{printf "%s\t%d\t%s\n",$1,$2, VAR}' chrom.sizes > bed/chromInfo/chromInfo.tab

# Step 6

echo "Creating the $BASE_NAME database..."

hgsql -e "create database $BASE_NAME ;" mysql

# Step 7

echo "Adding the GRP table to the $BASE_NAME database..."

hgsql $BASE_NAME < $GB_SOURCE/kent/src/hg/lib/grp.sql

# Step 8
 
echo "Loading $BASE_NAME chromInfo into database..."

hgLoadSqlTab $BASE_NAME chromInfo $GB_SOURCE/kent/src/hg/lib/chromInfo.sql bed/chromInfo/chromInfo.tab

# Step 9

echo "Loading the $BASE_NAME gold and gap tables..."

hgGoldGapGl $BASE_NAME $AGP_FILE

# Step 10

if [[ ! -d bed ]] || [[ ! -d bed/gc5Base ]]; then
    echo "Creating gc5Base folder..."
    mkdir -p bed/gc5Base
fi

echo "Generating gc5Base data..."

hgGcPercent -wigOut -doGaps -file=stdout -win=5 -verbose=0 $BASE_NAME $TWO_BIT_NAME | wigEncode stdin bed/gc5Base/gc5base.{wig,wib}

hgLoadWiggle -pathPrefix=/gbdb/$BASE_NAME/wig $BASE_NAME gc5Base bed/gc5Base/gc5Base.wig

if [[ ! -d /gbdb/$BASE_NAME/wib ]]; then
    echo "Creating wib folder..."
    mkdir -p /gbdb/$BASE_NAME/wib
fi
 
ln -s `pwd`/bed/gc5Base/gc5Base.wib /gbdb/$BASE_NAME/wib

echo "returning to the main script to build SQL statements"

# Exeunt
exit 1
