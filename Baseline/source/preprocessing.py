import utils 
import numpy as np
#path='/home/pritamnath/stanford_nlp/a4'
train_en=utils.read_corpus('./bengali_corpus/bn-en/training.bn-en.en','tgt')
train_es=utils.read_corpus('./bengali_corpus/bn-en/training.bn-en.bn','src')


print(train_es)

train_en_padded=utils.pad_sents(train_en,"ami")
train_es_padded=utils.pad_sents(train_es,"ami")

print('bekar')
        
