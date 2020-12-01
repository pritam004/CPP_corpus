##this is by far the most important function file
## contains many useful utilities
## Hare Krishna

import json
import numpy as np
import pandas as pd
import git
import sys
import os 

## some_constants

web_url='https://www.github.com/'
folder_url='/scratch/pritamkumar/git_data/'
form = r'{%n  "commit": "%H",%n  "abbreviated_commit": "%h",%n  "tree": "%T",%n  "abbreviated_tree": "%t",%n  "parent": "%P",%n  "abbreviated_parent": "%p",%n  "refs": "%D",%n  "encoding": "%e",%n  "subject": "%s",%n  "sanitized_subject_line": "%f",%n  "body": "%b",%n  "commit_notes": "%N",%n  "verification_flag": "%G?",%n  "signer": "%GS",%n  "signer_key": "%GK",%n  "author": {%n    "name": "%aN",%n    "email": "%aE",%n    "date": "%aD"%n  },%n  "commiter": {%n    "name": "%cN",%n    "email": "%cE",%n    "date": "%cD"%n  }%n},'

## we need the info of where the file is stored in web and other meta data

df=pd.read_csv('/home/pritamkumar/selected_repos.csv')

## read the json file


file=open(sys.argv[1])
json_file=json.loads(json.load(file))


def give_base_name(file):
    '''
    @ gives the base file name after removing the local path
    33 is the length of the local path ,this will change depending on where the repos are cloned

    '''
    
    ##skip 33 characters and return
    
    return file[30:]

def is_parallel(file):
    '''
    @ checks whether the file contains description or not
    '''
    if 'Definition' in file['description']:
        return False
    else:
        return True

def give_repo_name(df,r_name):
    ''''
    @ gives the owner name along with repo name 
    '''
    for i in df['Name with Owner'].values:
        if r_name in i :
            return i
def get_commit_id(file):

    '''
    @gives the commit id of a particular git clone

    '''

    global form
    
    g = git.Git(file) 
    js=g.log(pretty=form)
    decoder = json.JSONDecoder(strict=False)
    commit_id=decoder.raw_decode(js)[0]['commit']
    return commit_id

def get_code(file,f):
    '''
    @get actual code snippet from a file
    '''
    start=int(file['start_line'])
    end=int(file['end_line'])
    code_list=[]
    for i in range(end):
        if(i>= start-2):
            c=f.readline()
            print(i,c)
            code_list.append(c)
        else:
            f.readline()
    fn_name=file['function_name'].replace('(','').replace(')','')
    print(fn_name)

    line_no=0
    if fn_name in code_list[0]:
        line_no=0
    elif fn_name in code_list[1]:
        line_no=1
    else:
        line_no=-1 ## error the function was not found in the specified location
    print(line_no)
    if line_no!=-1:
        code=''
        for i in range(line_no,len(code_list)):
            code+=code_list[i]
        return code
    else:
        return line_no

def get_license(r_name):
    global df
    for i in range (len(df['Name with Owner'].values)):
        if r_name in df['Name with Owner'].values[i]:
            return df['License'].values[i]

def is_cpp(name):
    '''
    @checks if the file is cpp or not
    '''
    if '.cpp' in name or '.h' in name:
        return 1
    return 0
g_name=''
if __name__ =='__main__':

    parallel_corpus=[]
    mono_corpus=[]
    down_url='https://raw.githubusercontent.com/'
    residue=[]
    print(folder_url+sys.argv[1][32:-5])
    commit_id=get_commit_id(folder_url+sys.argv[1][32:-5])

    for file_ in json_file:
        try:
            s=give_base_name(file_['file_name'])
            print(s)
            #s=s[1:]
            di=s.find('/')
            r_name=s[0:di]
            print(r_name)
            b_name=s[di:]
            cpp=is_cpp(b_name)
            g_name=r_name
            if cpp==0:   ##some other extention
                continue

            f=f=open(folder_url+give_base_name(file_['file_name']))
            code=get_code(file_,f)
            
            license=get_license(r_name)
            if code !=-1:
                if is_parallel(file_):
                    parallel_corpus.append(
                    
                    {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'description': file_['description'],
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': web_url+give_repo_name(df,r_name)+'/blob/'+commit_id+b_name,
                        'download_link':down_url+give_repo_name(df,r_name)+'/'+commit_id+b_name,
                        'code': code,
                        'license':license
                        
                
                    })
                    print(

                            {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'description': file_['description'],
                        'start_line': file_['start_line'],
                        'download_link':down_url+give_repo_name(df,r_name)+'/'+commit_id+b_name,
                        'end_line':file_['end_line'],
                        'file_name': web_url+give_repo_name(df,r_name)+'/blob'+'/'+commit_id+b_name,
                        'code': code,
                        'license':license
                    }

                    )
                else :
                    mono_corpus.append(
                        {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'download_link':down_url+give_repo_name(df,r_name)+'/'+commit_id+b_name,
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': web_url+give_repo_name(df,r_name)+'/blob'+'/'+commit_id+b_name,
                        'code': code,
                        'license':license
                        }

                    )
                    print(

                        {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'download_link':down_url+give_repo_name(df,r_name)+'/'+commit_id+b_name,
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': web_url+give_repo_name(df,r_name)+'/blob'+'/'+commit_id+b_name,
                        'code': code,
                        'license':license
                        }

                    )
            else:
                residue.append(
                 {
                        'function_name': file_['function_name'],
                        'description': file_['description'],
                        'signature': file_['signature'] ,
                        'download_link':down_url+give_repo_name(df,r_name)+'/'+commit_id+b_name,
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': web_url+give_repo_name(df,r_name)+'/blob'+'/'+commit_id+b_name,
                        'code':'',
                        'license':license,
                        'disk_file_name':file_['file_name']
                        }
                
                )
        except:
            pass
    r_name=g_name
    f1=open('/scratch/pritamkumar/para/'+r_name+'.parallel.json','w')
    json.dump(parallel_corpus,f1)
    f2=open('/scratch/pritamkumar/mono/'+r_name+'.mono.json','w')
    json.dump(mono_corpus,f2)
    f3=open('/scratch/pritamkumar/residue/'+r_name+'.residue.json','w')
    json.dump(residue,f3)
    
    
    

    



