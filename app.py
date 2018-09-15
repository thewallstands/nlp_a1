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


file_trump_train = (r"C:\Users/13695\Documents\Nature_language_processing/a1/train/trump.txt")
file_obama_train = (r"C:\Users/13695\Documents\Nature_language_processing/a1/train/obama.txt")
file_trump_dev = (r"C:\Users/13695\Documents\Nature_language_processing/a1/development/trump.txt")
file_obama_dev = (r"C:\Users/13695\Documents\Nature_language_processing/a1/development/obama.txt")

perplexity_trump=ngrammodel.train(r"train/trump",r"development/trump",2)
print(perplexity_trump)
