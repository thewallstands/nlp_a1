"""
User interface for module ngrammodel

When run as a script, this module calculates the n-gram model and execute the
things we want to do.

Author: Tianli Xia
Date:   Sep 11th, 2018
"""

import introcs
import ngrammodel
import string

file_trump_train = open(r"C:\Users/13695\Documents\Nature_language_processing/a1/train/trump.txt", "r", encoding='utf-8')
file_obama_train = open(r"C:\Users/13695\Documents\Nature_language_processing/a1/train/obama.txt", "r", encoding='utf-8')
file_trump_dev = open(r"C:\Users/13695\Documents\Nature_language_processing/a1/development/trump.txt", "r", encoding='utf-8')
file_obama_dev = open(r"C:\Users/13695\Documents\Nature_language_processing/a1/development/obama.txt", "r", encoding='utf-8')
trump= file_trump_train.read()
obama= file_obama_train.read()
trump_dev= file_trump_dev.read()
obama_dev= file_obama_dev.read()
file_trump_train.close()
file_obama_train.close()
file_trump_dev.close()
file_obama_dev.close()
#trump= ngrammodel.prep(trump, 1)
#obama= ngrammodel.prep(obama, 1)
dict_uni_trump= ngrammodel.ngrams(trump, 1, 0)
dict_uni_obama= ngrammodel.ngrams(obama, 1, 0)
dict_bi_trump= ngrammodel.ngrams(trump, 2, 0)
dict_bi_obama= ngrammodel.ngrams(obama, 2, 0)
dict_uni_trump_dev= ngrammodel.ngrams(trump_dev, 1, 0)
dict_uni_obama_dev= ngrammodel.ngrams(obama_dev, 1, 0)
dict_bi_trump_dev= ngrammodel.ngrams(trump_dev, 2, 0)
dict_bi_obama_dev= ngrammodel.ngrams(obama_dev, 2, 0)
dict_bi_smooth_trump= ngrammodel.bismooth(dict_bi_trump, dict_uni_trump, dict_uni_trump_dev)
dict_bi_smooth_obama= ngrammodel.bismooth(dict_bi_obama, dict_uni_obama, dict_uni_obama_dev)

perplexity_trump= ngrammodel.perplexity(dict_bi_trump_dev, dict_bi_smooth_trump)
perplexity_obama= ngrammodel.perplexity(dict_bi_obama_dev, dict_bi_smooth_obama)
print(perplexity_trump)
print(perplexity_obama)
