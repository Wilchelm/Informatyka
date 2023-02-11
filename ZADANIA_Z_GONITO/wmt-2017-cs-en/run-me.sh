#!/bin/bash

MARIAN=$HOME/amun

if [ ! -e $MARIAN/build/amun ]
then
    echo "amun is not installed in $MARIAN/build, you need to compile the toolkit first"
    exit 1
fi

if [ ! -e $HOME/amun/examples/tools/moses-scripts ] || [ ! -e $HOME/amun/examples/tools/sacreBLEU ]
then
    echo "missing tools in $HOME/amun/examples/tools, you need to download them first"
    exit 1
fi

if [ ! -e "$HOME/amun/examples/translating-amun/cs-en/model.npz" ];
then
    wget -r -l 1 --cut-dirs=2 -e robots=off -nH -np -R index.html* http://data.statmt.org/rsennrich/wmt16_systems/cs-en/
fi

# create configuration file for model ensemble
$MARIAN/build/amun -m $HOME/amun/examples/translating-amun/cs-en/model-ens?.npz -s $HOME/amun/examples/translating-amun/cs-en/vocab.cs.json -t $HOME/amun/examples/translating-amun/cs-en/vocab.en.json \
    --mini-batch 1 --maxi-batch 1  --cpu-threads 4 -b 12 -n --bpe $HOME/amun/examples/translating-amun/cs-en/csen.bpe \
    --relative-paths --dump-config > ensemble.yml

# translate test set with ensemble
cat dev-0/in.tsv | \
    # preprocess
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/normalize-punctuation.perl -l cs | \
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/tokenizer.perl -l cs -penn | \
    $HOME/amun/examples/tools/moses-scripts/scripts/recaser/truecase.perl -model $HOME/amun/examples/translating-amun/cs-en/truecase-model.cs | \
    # translate
    $MARIAN/build/amun -c ensemble.yml --cpu-threads 4 | \
    # postprocess
    $HOME/amun/examples/tools/moses-scripts/scripts/recaser/detruecase.perl | \
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/detokenizer.perl -l en > dev-0/out.tsv

# translate test set with ensemble
cat test-A/in.tsv | \
    # preprocess
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/normalize-punctuation.perl -l cs | \
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/tokenizer.perl -l cs -penn | \
    $HOME/amun/examples/tools/moses-scripts/scripts/recaser/truecase.perl -model $HOME/amun/examples/translating-amun/cs-en/truecase-model.cs | \
    # translate
    $MARIAN/build/amun -c ensemble.yml --cpu-threads 4 | \
    # postprocess
    $HOME/amun/examples/tools/moses-scripts/scripts/recaser/detruecase.perl | \
    $HOME/amun/examples/tools/moses-scripts/scripts/tokenizer/detokenizer.perl -l en > test-A/out.tsv

