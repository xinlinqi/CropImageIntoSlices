#-*- coding: utf-8 -*-
import os
import json

FILE_NAME = "weibo_item.json"
RESULT_FILE = "result.txt"
FILE_SIZE = 1000

try:
	f = open(FILE_NAME)
except:
	print "ERROR: please put the input file named ", FILE_NAME, "INTO the dir where this program lies."
r = open(RESULT_FILE, "w")
line = f.readline()
print '*'*3, 'Transfrom start', '*'*3 
print 'Please wait for a few seconds........'
r.write( ",".join(json.loads(line).keys()) + '\n')
while line:
	obj = json.loads(line)
	val = (",").join(unicode(v) for v in obj.values()).encode('utf-8')
	r.write(val + '\n')
	line = f.readline()
print '*'*3, 'Transfrom ended', '*'*3
print 'Result lies in the "', RESULT_FILE , '" under the same dir'
r.close()