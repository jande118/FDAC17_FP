#!/usr/local/bin/python3

import sys

# Check for one input argument
if len(sys.argv) != 2:
    print('Usage: reindex [name of index file to reindex]')
    sys.exit()


filename = str(sys.argv[1])
outfile = filename + '.reindex'

runningTotal = 0
with open(filename,'r') as ifp, open(outfile,'w') as ofp:
    for line in ifp:
        tokens = line.split() # break apart line by unspecified whitespaces
        currentPackage= tokens[1]
        lastIndex=runningTotal
        runningTotal+=int(tokens[0])
        
        # save output at end of output file
        ofp.write(str(currentPackage)+','+str(lastIndex+1)+','+str(runningTotal)+'\n')

