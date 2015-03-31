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
def add_to_database(row):
    '''
    Here we extract the information and put it into the database
        - the file should have everything that we need but don't have
        - Dr Pip Griffen and Lachlan decided that in our instance we didn't
          need Gene Sorter, so hgNearOk can be 0, dbDb.orderKey and 
          genomeClade.priority could just be incremental, correspondence with
          the GB email list member Steve revealed that hgPbOk was deprecated
          and should always be 0 
    '''
    sql_insert = dict(fn = row[0], 
    name = row[1],
    desc = row[2], 
    nib = "/gbdb/%s" % row[1],
    organism = row[3],
    defaultPos = row[4],
    active = 1, # we presume uploaded data is wanted data.
    orderKey = rownum,
    genome = row[5],
    scientificName = row[6], 
    htmlPath = "/gbdb/%s/html/description.html" % row[1],
    hgNearOk = 0,
    hgPbOk = 0,
    sourceName = row[7],
    taxId = row[8])
    return sql_insert


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
            sql_insert = add_to_database(row)
            print sql_insert['name'], sql_insert['taxId'], sql_insert['htmlPath']
            print sql_insert
        rownum += 1
        


finally:
    f.close()


# Step 11

#"""
#SQL="INSERT INTO dbDb (name, description, nibPath, organism, defaultPos, active, orderKey, genome, scientificName, htmlPath, hgNearOk, hgPbOk, sourceName, taxId) VALUES (\"$BASE_NAME\","
#
#"""
