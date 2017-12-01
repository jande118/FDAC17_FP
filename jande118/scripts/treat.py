#! /usr/bin/env python3

# NOT WORKING

# Check commandline arguments
'''
import sys
if len(sys.argv) != 4:
    print('usage: ./treat.py [source file] [target file] [package name]')
    sys.exit()
IN = str(sys.argv[1])
OUT = str(sys.argv[2])
NAME = str(sys.argv[3])
HEADER = str('ID,Platform,Project Name,Project ID,Version Number,Version ID,Dependency Name,Dependency Platform,Dependency Kind,Optional Dependency,Dependency Requirements,Dependency Project ID')
#egrep "^([^,]+,){1}Dub,"
print(sys.argv[0],IN, OUT, NAME)
with open(IN, 'r') as inf, open(OUT, 'w') as ofp:
    for line in inf:
        tokens = line.split(',')
        if tokens[1] == NAME: ofp.write(line)
'''