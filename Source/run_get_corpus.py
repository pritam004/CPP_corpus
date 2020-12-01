import os
import sys
from os import listdir
from os.path import isfile, join
mypath='/scratch/pritamkumar/json_files'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    print('python get_corpus.py '+mypath+'/'+f)
    os.system('python get_corpus.py '+mypath+'/'+f)
