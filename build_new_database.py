#!/usr/bin/python

import MySQLdb
import re
import os
import csv
import sys

if len(sys.argv) != 2:
    print "usage: build_new_database.py <filename>"
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print "%s is not a file" % sys.argv[1]
    print "usage: build_new_database.py <filename>"
    sys.exit()

# setting up the MySQL connection
db = MySQLdb.connect(host="localhost", user="root", passwd="browser", db="hgcentral")
dbcursor = db.cursor()

f = open(sys.argv[1], 'rb')
try:
    reader = csv.reader(f)
    rownum = 0
    for row in reader:
        if rownum == 0:
            header = row
        else:
            #filename = row[0]
            sql_dict = { "name": "%s" % row[1], "desc": "%s" % row[2], "nib": "/gbdb/%s" % row[1], "organism": "%s" % row[3], "defaultPos": "%s" % row[4], "active": 1, "orderKey": rownum, "genome": "%s" % row[5], "scientificName": "%s" % row[6], "htmlPath": "/gbdb/%s/html/description.html" % row[1], "hgNearOk": 0, "hgPbOk": 0, "sourceName": "%s" % row[7], "taxId": "%s" % row[8] }
	
            dbcursor.execute("""INSERT INTO dbDb (name, description, nibPath, organism, defaultPos, active, orderKey, genome, scientificName, htmlPath, hgNearOk, hgPbOk, sourceName, taxId) VALUES (%(name)s, %(desc)s, %(nib)s, %(organism)s, %(defaultPos)s, %(active)s, %(orderKey)s, %(genome)s, %(scientificName)s, %(htmlPath)s, %(hgNearOk)s, %(hgPbOk)s, %(sourceName)s, %(taxId)s)""", sql_dict)
    
        rownum += 1
        


finally:
    f.close()


# Step 11

#"""
#SQL="INSERT INTO dbDb (name, description, nibPath, organism, defaultPos, active, orderKey, genome, scientificName, htmlPath, hgNearOk, hgPbOk, sourceName, taxId) VALUES (\"$BASE_NAME\","
#
#"""
