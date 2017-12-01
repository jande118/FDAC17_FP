import sys
import subprocess

if len(sys.argv) < 2:
    print('usage:   python3 process.py [dependency #1] [dependency #2] ...')
    print('example: python3 process.py CRAN Dub')
    sys.exit()

DATA = '../data/extracted/dependencies.csv'
for dep in sys.argv:
    if dep == sys.argv[0]: # ignore process.py and dependency.csv
        continue
    OUT = '../data/new_data/' + dep + '.data' # Build output file
    egrep = 'egrep \"^([^,]+,){1}' + dep + ',\" ' + DATA + ' > ' + OUT # Build the egrep command
    cmd = [egrep]
    #print(DATA); print(egrep); print(cmd) # DEBUGGING
    print(subprocess.check_output(cmd, shell=True))