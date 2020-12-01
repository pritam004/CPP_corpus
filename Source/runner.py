import subprocess
import os
import sys



from joblib import Parallel, delayed
import concurrent.futures
import urllib.request


file='lld'
src='/scratch/pritamkumar/git_data/'
import re
folder='/scratch/pritamkumar/git_data/'
subfolders = [ f.name for f in os.scandir(folder) if f.is_dir() ]

subfolders=subfolders[int(sys.argv[1]):int(sys.argv[2])]

def run_func(f):
    c='bash /home/pritamkumar/generation_script.sh '
    s='python /home/pritamkumar/scrapper.py '
    path=src+f
    caller=c+'/scratch/pritamkumar/doxygen_files/'+f+' '+path
    scrapper=s+'/scratch/pritamkumar/doxygen_files/'+f+' '+f

    os.system(caller)
    os.system(scrapper)




URLS=subfolders
with concurrent.futures.ThreadPoolExecutor(max_workers=224) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(run_func, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except:
            #print('exception occured')
            pass
