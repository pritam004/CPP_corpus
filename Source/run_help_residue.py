import os
import sys
from os import listdir
from os.path import isfile, join
mypath='/scratch/pritamkumar/residue'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
     try :
          os.system('python help_residue.py '+f)
     except:
          pass