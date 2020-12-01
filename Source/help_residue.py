import json
import pandas as pd
import numpy as np
import git
import sys

f=open('/scratch/pritamkumar/residue/'+sys.argv[1])
json_file=json.load(f)

N=len(json_file)


web_url='https://www.github.com/'
down_url='https://raw.githubusercontent.com/'
folder_url='data/'
form = r'{%n  "commit": "%H",%n  "abbreviated_commit": "%h",%n  "tree": "%T",%n  "abbreviated_tree": "%t",%n  "parent": "%P",%n  "abbreviated_parent": "%p",%n  "refs": "%D",%n  "encoding": "%e",%n  "subject": "%s",%n  "sanitized_subject_line": "%f",%n  "body": "%b",%n  "commit_notes": "%N",%n  "verification_flag": "%G?",%n  "signer": "%GS",%n  "signer_key": "%GK",%n  "author": {%n    "name": "%aN",%n    "email": "%aE",%n    "date": "%aD"%n  },%n  "commiter": {%n    "name": "%cN",%n    "email": "%cE",%n    "date": "%cD"%n  }%n},'

## we need the info of where the file is stored in web and other meta data

df=pd.read_csv('selected_repos.csv')
def is_cpp(name):
    '''
    @checks if the file is cpp or not
    '''
    if '.cpp' in name or '.h' in name:
        return 1
    return 0
def is_parallel(file):
    '''
    @ checks whether the file contains description or not
    '''
    if 'Definition' in file['description']:
        return False
    else:
        return True
def get_code_string(code_list):
    code=''
    for i in code_list:
        code+=i
    return code
def get_code(file,f):
    '''
    @get actual code snippet from a file
    '''
    start=int(file['start_line'])
    end=int(file['end_line'])
    code_list=[]
    for i in range(end - 1):
        if(i>= start-2):
            c=f.readline()
            #print(i,c)
            code_list.append(c)
        else:
            f.readline()
    return code_list



name_list=[]
line_no=[]
for i in range(N):
    file=json_file[i]
    f=open(file['disk_file_name'])
    fn_name=file['function_name'].replace('(','').replace(')','')
    desc=file['description']
    name_list.append({
        
        'name': fn_name,
        'description': desc,
        'signature':file['signature']
    })
    line_no.append({
        'code':get_code(file,f),
        'start': file['start_line'],
        'end':file['end_line'],
        'disk_file_name':file['disk_file_name'],
        'license':file['license'],
        'download_link':file['download_link'],
        'file_name':file['file_name']
        
        
    })
    
print(len(name_list))
print(len(line_no))

final_repo=[]
print(name_list[6])
print(line_no[6])

for i in range (N):
    #print('------------------------------------------------')
    for j in range(N):
        #print(((name_list[i]['name'] in line_no[j]['code'][0]) and line_no[j]['code'][0][0]!='/') or ((name_list[i]['name'] in line_no[j]['code'][1] )and line_no[j]['code'][1][0]!='/'))
       # print(line_no[j]['code'][0],name_list[i]['name'])
        if ((name_list[i]['name'] in line_no[j]['code'][0]) and line_no[j]['code'][0][0]!='/') or len(line_no[j]['code'])>1 and ((name_list[i]['name'] in line_no[j]['code'][1] )and line_no[j]['code'][1][0]!='/')  :
            final_repo.append({
            'function_name': name_list[i]['name'],
            'signature':name_list[i]['signature'],
                'description':name_list[i]['description'],
                'start_line': line_no[j]['start'],
                'end_line':line_no[j]['end'],
                'code':line_no[j]['code'],
                'file_name':line_no[j]['file_name'],
                'disk_file_name':line_no[j]['disk_file_name'],
            'license':line_no[j]['license'],
            'download_link':line_no[j]['download_link'],
                
            })
            
            break

parallel_corpus=[]
mono_corpus=[]

for file_ in final_repo:
            

            cpp=is_cpp(file_['file_name'])
            if cpp==0:   ##some other extention
                continue

            #f=f=open(folder_url+give_base_name(file_['file_name']))
            code=get_code_string(file_['code'])
            
            #license=get_license(r_name)
            if code !=-1:
                if is_parallel(file_):
                    parallel_corpus.append(
                    
                    {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'description': file_['description'],
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': file_['file_name'],
                        'download_link':file_['download_link'],
                        'code': code,
                        'license':file_['license']
                        
                
                    })
                    print(

                           {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'description': file_['description'],
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': file_['file_name'],
                        'download_link':file_['download_link'],
                        'code': code,
                        'license':file_['license']
                        
                
                    }

                    )
                else :
                    mono_corpus.append(
                        {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': file_['file_name'],
                        'download_link':file_['download_link'],
                        'code': code,
                        'license':file_['license']
                        }

                    )
                    print(

                        {
                        'function_name': file_['function_name'],
                        'signature': file_['signature'] ,
                        'start_line': file_['start_line'],
                        'end_line':file_['end_line'],
                        'file_name': file_['file_name'],
                        'download_link':file_['download_link'],
                        'code': code,
                        'license':file_['license']
                        }

                    )
       # except:
        #    print('exception')
        #    pass
print(f'parallel corpus legth{len(parallel_corpus)}')
print(f'mono corpus legth{len(mono_corpus)}')
f1=open('/scratch/pritamkumar/help_res_para/'+sys.argv[1]+'residue.parallel.json','w')
json.dump(parallel_corpus,f1)
f2=open('/scratch/pritamkumar/help_res_mono/'+sys.argv[1]+'residual.mono.json','w')
json.dump(mono_corpus,f2)