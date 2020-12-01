'''
This is the scraper file. 
This contains codes to convert the doxyfiles to the corresponding parallel files.
It is saved in the json file format

'''

from bs4 import BeautifulSoup
import sys
import json



def get_file_name(file_list,file_name):
    f=''
    for j in file_list:
        if file_name in j:
            f=j
    return f
    
def get_function_details(k ,soup): 
    files_list=[]
    for i in soup.find_all('li'):
        files_list.append(i.text)
    #print(files_list)
    
    function_name=soup.find_all('h2',class_='memtitle')[k].text[2:] # get the function name
    print(function_name)
    description=soup.find_all('div',class_='memitem')[k].p.text #get the docstring 
    print(description)
    start_line=int(soup.find_all('div',class_='fragment')[k].find_all('div',class_='line')[0].span.text) #get start line
    print(start_line)
    end_line=int(soup.find_all('div',class_='fragment')[k].find_all('div',class_='line')[-1].span.text) #get end line
    print(end_line)
    file_name=soup.find_all('p',class_='definition')[k].text.split()[-1][:-1] #get file name

    ##getting code is implemented later
    ##this one just gives the body of the code
    try:
        code=get_code(soup.find_all('div',class_='fragment')[k])
    except:
        code=''
    
   
    full_file_name=get_file_name(files_list,file_name)
    try:
        signature=soup.find_all('div',class_='memitem')[k].find_all('table',class_='mlabels')[0].find_all('table',class_='memname')[0].find_all('td')[0].text
        ##get the function signature
    
    except:
        signature=''

    ##return all the function details

    return {'function_name':function_name,'signature':signature,'description':description,'start_line':start_line,'end_line':end_line,
            'file_name':full_file_name,'code':code,'defn': soup.find_all('p',class_='definition')[k].text}

from os import listdir

##take only the html files
mypath=sys.argv[1]+'/html'

## get all the class html files
from os.path import isfile, join
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

final_list=[]
k=0

for i in onlyfiles:

    try:
        if 'class' in i and 'member' not in i and '.html' in i:

            f=open(mypath+ '/' + i)
            
            
            g=f.read()
            soup = BeautifulSoup(g,'html.parser')
         
            for J in range(len(soup.find_all('h2',class_='memtitle'))):
                
                print(str(get_function_details(J,soup))+'\n')
                final_list.append(get_function_details(J,soup))
            
            
    except:
       
        pass
    
print(len(final_list))
json_object = json.dumps(final_list, indent = 4)  

##dumps the final collected json files
f=open('/scratch/pritamkumar/json_files/'+sys.argv[2]+'.json','w')
json.dump(json_object,f)

