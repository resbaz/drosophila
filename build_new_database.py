#!/usr/bin/python

import MySQLdb
import re
import os
import csv




# Step 11

SQL="INSERT INTO dbDb (name, description, nibPath, organism, defaultPos, active, orderKey, genome, scientificName, htmlPath, hgNearOk, hgPbOk, sourceName, taxId) VALUES (\"$BASE_NAME\","

NIBPATH=\"/gbdb/$BASE_NAME\",
ACTIVE=1,
ORDERKEY=090321321,
HTMLPATH=\"/gbdb/$BASE_NAME/html/description.html\",
HGNEAROK=0,
HGPBOK=0,

DESC=\"D. Birchii\",
ORGANISM=\"Drosophila birchii\",
DEFAULTPOS="scaffold1:0-1000000",
GENOME=\"Drosophila birchii\",
SCIENTIFICNAME=\"Drosophila birchii\",
SOURCENAME=\"Genomic Basis for Adaptation to Climate Change Project\",
TAXID="46829",

SQL=$SQL$DESC$NIBPATH$ORGANISM$DEFAULTPOS$ACTIVE$ORDERKEY$GENOME$SCIENTIFICNAME$HTMLPATH$HGNEAROK$HGPBOK$SOURCENAME$TAXID


