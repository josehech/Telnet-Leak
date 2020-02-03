#!/usr/bin/python3
import pickle
import sys
    
with open('ipdict.pickle', 'rb') as handle:
    readdict = pickle.load(handle)

if sys.argv[1] in readdict.keys():
    sys.stdout.write("\033[1;31m")
    print('[✗] Leak contains IP')
else:
    sys.stdout.write("\033[1;32m")
    print('[✔] Leak does not contains IP')
