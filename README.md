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

## Baseline

We also provide a lstm-attention-translation-model as a baseline.It is in the Baseline folder.

It achieves a BLUE of 25 on a deduplicated test set of 10,000 samples.We have made sure that the test set is unique and it is not a subset of the train set, but the train set may contain duplicates.

The codes for that part I have borrowed from the standford course 224N on DLNLP ,assignment 3 and the code is my solution of the assignment but the utils files are those provided by the instructors.


