
Twitter Sentiment Analysis
================================

Guess the sentiment for texts in English.

Classes
-------

* `1` — positive sentiment
* `0` — negative sentiment

Directory structure
-------------------

* `README.md` — this file
* `config.txt` — configuration file
* `train/` — directory with training data
* `train/train.tsv` — train set, (text - 1st column, sentiment - 2nd column)
  a text fragment in the second one
* `dev-0/` — directory with dev (test) data
* `dev-0/in.tsv` — input data for the dev set (text fragments)
* `dev-0/expected.tsv` — expected (reference) data for the dev set
* `test-A` — directory with test data
* `test-A/in.tsv` — input data for the test set (text fragments)
* `test-A/expected.tsv` — expected (reference) data for the test set (hidden)
