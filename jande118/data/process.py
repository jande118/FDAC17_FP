import sys
import subprocess

if len(sys.argv) < 2:
    print('usage: python3 ./process.py [dependency file path] [dependency #1] [dependency #2] ...')
    sys.exit()
DATA = str(sys.argv[1])
for dep in sys.argv:
    if dep == sys.argv[0] or dep == sys.argv[1]: # ignore process.py and dependency.csv
        continue
    OUT = dep + '.data' # Build output file
    cmd = 'egrep \"^([^,]+,){1}' + dep + ',\" '+ DATA + ' > ' + OUT # Build command
    print(subprocess.check_output([cmd], shell=True))
