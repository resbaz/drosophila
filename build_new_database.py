#!/usr/bin/python

import MySQLdb
import re
import os
import csv
import sys

# setting up the MySQL connection
#db = MySQL.connect(host="localhost", user="ubuntu", password="browser", db="dbDb")
#curr = db.cursor()

# getting the data from the csv

if len(sys.argv) != 2:
    print "usage: build_new_database.py <filename>"
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print "%s is not a file" % sys.argv[1]
    print "usage: build_new_database.py <filename>"
    sys.exit()

f = open(sys.argv[1], 'rb')
try:
    reader = csv.reader(f)
    rownum = 0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            print row
            fn = row[0] 
            name = row[1]
            desc = row[2] 

        rownum += 1
finally:
    f.close()


# Step 11

#"""
#'''
#SQL="INSERT INTO dbDb (name, description, nibPath, organism, defaultPos, active, orderKey, genome, scientificName, htmlPath, hgNearOk, hgPbOk, sourceName, taxId) VALUES (\"$BASE_NAME\","
#
#NIBPATH=\"/gbdb/$BASE_NAME\",
#ACTIVE=1,
#ORDERKEY=090321321,
#HTMLPATH=\"/gbdb/$BASE_NAME/html/description.html\",
#HGNEAROK=0,
#HGPBOK=0,
#
#DESC=\"D. Birchii\",
#ORGANISM=\"Drosophila birchii\",
#DEFAULTPOS="scaffold1:0-1000000",
#GENOME=\"Drosophila birchii\",
#SCIENTIFICNAME=\"Drosophila birchii\",
#SOURCENAME=\"Genomic Basis for Adaptation to Climate Change Project\",
#TAXID="46829",
#
#SQL=$SQL$DESC$NIBPATH$ORGANISM$DEFAULTPOS$ACTIVE$ORDERKEY$GENOME$SCIENTIFICNAME$HTMLPATH$HGNEAROK$HGPBOK$SOURCENAME$TAXID
#'''
#"""
