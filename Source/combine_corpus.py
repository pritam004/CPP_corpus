import os
import sys
from os import listdir
from os.path import isfile, join
import json
mypath=sys.argv[1]
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
big_list=[]
for f in onlyfiles:
    file=open(mypath+'/'+f)
    file_json=json.load(file)
    big_list.extend(file_json)

print(len(big_list))


    
fw=open(sys.argv[1]+'final_json.json','w')
json.dump(big_list,fw)