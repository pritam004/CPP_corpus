#!/bin/bash

if [ "$1" = "train" ]; then
	python run.py train --train-src=../data/code_train.txt --train-tgt=../data/doc_train.txt --dev-src=../data/code_valid.txt --dev-tgt=../data/doc_valid.txt --vocab=vocab.json --cuda
elif [ "$1" = "test" ]; then
    mkdir outputs
    touch outputs/test_outputs.txt
    python run.py decode model.bin ../data/code_test_no.txt ../data/doc_test_no.txt outputs/test_outputs.txt --cuda
elif [ "$1" = "train_local" ]; then
	python run.py train --train-src=./en_es_data/train.es --train-tgt=./en_es_data/train.en --dev-src=./en_es_data/dev.es --dev-tgt=./en_es_data/dev.en --vocab=vocab.json
elif [ "$1" = "test_local" ]; then
    python run.py decode model.bin ./en_es_data/test.es ./en_es_data/test.en outputs/test_outputs.txt
elif [ "$1" = "vocab" ]; then
	python vocab.py --train-src=../data/cs_code_train.txt --train-tgt=../data/doc_train.txt vocab.json
else
	echo "Invalid Option Selected"
fi
