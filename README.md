# CPP_PRALLEL_CORPUS
We introduce a new parallel corpus for the C-Plus-Plus language .

A parallel corpus comprising of a code snippet and the corresponding natural language description can be of great advantage. This can be used for creating several useful productivity tools like code generation, code completion, code summarization, CODE SEARCH etc. We see many such parallel corpus for the languages like Java, python, golang, JavaScript, BASH what we propose is to prepare one such corpus for c++ programming language. 
We would be specifically targeting the code summarization task i.e. given a code the model is required to generate a natural language description of it. 



## Data Preparation Cycle

![data_cycle](https://github.com/pritam004/CPP_corpus/blob/main/process.png?raw=true)


## Download links and Statistics

|PART-ID | MONO | GOOD PARA |BAD PARA|
|:---:|:---:|:---:|:---:|
|1|[487290](https://drive.google.com/file/d/1nL3RlGsbjCF8d5PK57o5XmwfdBUFucIG/view?usp=sharing)|[127977](https://drive.google.com/file/d/141ZHZiLkzoXjBjFd2iun6ukLfhey9xFK/view?usp=sharing)|[81704](https://drive.google.com/file/d/1M6xlaekc3N5RdQ4bJPGWmiSHqmOp8y0G/view?usp=sharing)|
|2|[561590](https://drive.google.com/file/d/1oPNX3UNSTeyTK610PL21ciS1450NShOq/view?usp=sharing)|[178075](https://drive.google.com/file/d/1Qt79_ismezyRXfGMu_DF8T8u5RwjdtaK/view?usp=sharing)|[111788](https://drive.google.com/file/d/1_ty2FTBdHOeXZTn2sF3BhjzkKJXY6DSf/view?usp=sharing)|
|3|[470246](https://drive.google.com/file/d/1rYwr0YMworAAaCQ8XgGkPJkF8355aPrU/view?usp=sharing)|[168927](https://drive.google.com/file/d/1KZ14nVbO-RqoqFwpI17YotB2k44NmYbC/view?usp=sharing)|[90165](https://drive.google.com/file/d/1HCCxlEKD9b_ZRz3hIvr3X09FbWsWz9p3/view?usp=sharing)|
|4|[484018](https://drive.google.com/file/d/1RsBu8HBQgTD8YitR5eP9MJmh3sCLJaPe/view?usp=sharing)|[145623](https://drive.google.com/file/d/1-4MerqavZVeC32gBeTpDn65TfJXVCfm2/view?usp=sharing)|[89253](https://drive.google.com/file/d/1WqZ4w3OD3Zi0Ulq2zNI9YVI7GB08MR6k/view?usp=sharing)
|5|[466051](https://drive.google.com/file/d/1rgFdADUvnz6uROMaxjDHesejguO0v30D/view?usp=sharing)|[190387](https://drive.google.com/file/d/1tvgGBeFHZb5gAYgnRwbhm7KU6Lf31op5/view?usp=sharing)|[89400](https://drive.google.com/file/d/1yGTkjf6yvd6XpZ76DALBF_OGYHEzCPuW/view?usp=sharing)|
|6|[524742](https://drive.google.com/file/d/1kKLTMLjNYg6HGnk6MLzcNUD-yRvKu7gW/view?usp=sharing)|[157997](https://drive.google.com/file/d/1chuejr79e12iLKjwEOKEgCIlIpElxY6l/view?usp=sharing)|[108132](https://drive.google.com/file/d/1OogCvDDbsA0wgQMC0uQ-YMEt9We6v6MN/view?usp=sharing)|

The mono contains unilateral corpus containing only code snippets extracted from the github repositories, while the good para consists of good doctrings along with code. A lot of rules were applied after seeing the data and the bad examples were seperated and given as a separate data. A detailed description of different fields in the data is given at a later section.

*A couple of more parts are under process and it will be added soon






Exact matching deduplication was carried out on about half of the data. Then the data was seperated into train,validate, test sets.This was used for training the model.


The tokenization used was simple whitespace tokenizer which is used in many architectures.Since it is a simple baseline model it solves our purpose here but for more advanced models seperate processing needs to be performed.After white space tokenization the camel and the snake case were parsed in the code. The vocabulary for the train set can be found [here](https://drive.google.com/file/d/1QSCAKzbI5S1sjSJJUtmI1NCSfGjBcxq1/view?usp=sharing). This is what we use for buiding the model.

In the following section we provide the clean deduplicated data which is around half of the total data given in the previous section.

|part|no of samples|link|
|:---:|:---:|:---:|
|train|298,878|[link](https://drive.google.com/drive/folders/1J2luTosTvQ4RG5wWM9aEqMwRfI6qn53U?usp=sharing)|
|dev|33,209|[link](https://drive.google.com/drive/folders/1J2luTosTvQ4RG5wWM9aEqMwRfI6qn53U?usp=sharing)|
|test|83,022|[link]((https://drive.google.com/drive/folders/1J2luTosTvQ4RG5wWM9aEqMwRfI6qn53U?usp=sharing))|


## How to reproduce the dataset 

The steps are as follows and has to be carried out with exactness to reproduce the results. The data preparation life cycle can be referenced to understand it better. To make the processes efficient most of them have been parallelized and makes active use of multiple threads.

1. First step is to get the list of repositories that we want to use. For this task We have used   [libraries.io](libraries.io)   data dump and extract the relevant repositories with atleast 20 stars and some other heuristics. 
2. Install Doxygen, which is the core module in our experiments.

    2.1  <code>git clone https://github.com/doxygen/doxygen</code> 

    2.2 <code> git checkout 6922d5d63d77c8f640c58e9c68a9955f9f0aa9a7 </code> [This is important we need this specific commit]

    2.3 Build doxygen using the guide given in their website and set the environment paths.
3. Once we have the repositories and doxygen, run the runner.py 
   
    <code>python runner.py <number_of_repo></code>

    This calls first doxygen and the scrapper to dump the data in json. 
4. Next step is to generate the corpuses.

    4.1  <code>mkdir para mono residue</code>

    4.2  <code>python run_get_corpus.py</code>
5. Next step is to combine the corpus tp form a single file for mono and para respectively.

    5.1 <code>python combine_corpus.py para</code>

    5.2 <code>python combine_corpus.py mono</code>

## How does the dataset look

![data](https://github.com/pritam004/CPP_corpus/blob/main/data.PNG?raw=true)


## Dataset Description

<b>function name</b> This the name of the method .

<b>signature</b> This field contains return_type : class_name : namespace :function_name

<b>start_line</b> Start line of the code

<b>end_line</b> End line of the code

<b>file_name</b> This is a link to the file that contains the code on github.

<b>download_link</b>  This is the download link to the raw code file.

<b>code</b> This is the string version of the code.

<b> license</b> The license for the usage of the code.

## Allowed licenses


* 'apache-2.0',
* 'lgpl-2.1',
* 'epl-1.0',
* 'isc',
* 'bsd-3-clause',
* 'bsd-2-clause',
* 'mit',
* 'gpl-2.0',
* 'cc0-1.0',
* 'lgpl-3.0',
* 'mpl-2.0',
* 'unlicense',
* 'gpl-3.0'







