#to download all the repos

import pandas as pd

from joblib import Parallel, delayed
import git


df=pd.read_csv('/home/pritamkumar/selected_repos.csv')

def get_url(web,repo):
    name='https://'
    if web == 'GitHub':
        name+='github.com'
    else:
        name+='gitlab.com'
    name+='/'+repo
    return name

def downloader(i):
    
    print('downloading--------------->'+i+'\n')
    git.Git('/scratch/pritamkumar/git_data/').clone(i)


URLS=[get_url(df.values[i,1],df.values[i,2]) for i in range(len(df))]
#URLS=URLS[8000:9500]



import concurrent.futures
import urllib.request


# Retrieve a single page and report the URL and contents
def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(downloader, url): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try
        data = future.result()
        except:
            print('------exception occured-----')
            pass

