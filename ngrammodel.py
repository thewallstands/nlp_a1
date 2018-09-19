"""
Module for n-gram models.

This module completes the following tasks: read a text and convert it into a n-gram
model saved in a dictionary; count the (smoothed) probability of each possible token;
randomly generate some sentence.

Author: Tianli Xia
Date: Sep 12th, 2018
"""

import ngrammodel
import pandas
import string
import math
import numpy
import json

def prep(input):
    """
    Returns: a string which is preprocessed.

    Solve a bug in the original text: "don't" sometimes are seperated and become
    "do n't".

    Parameter input: original word corpus.

    Parameter k: a flag showing if we should remove all the punctuations. True if
    we remove all the punctuations.
    """
    input=input.lower()
    if (k==True):
        for c in string.punctuation:
            input=input.replace(c+' ','') # preserve the punctuations between words, such as "didn't"
        return output
    if (k==False):
        output=input
        return output


def ngrams(input, n, punc):
    """
    Returns: a dictionary store all the n-gram tokens (index) appearing in the input corpus
    and count the number of them (value).

    Parameter input: a string
    Precondition: (1) all lower case; (2) (optional)No punctuation in the string.

    Parameter n: a integer denoting which model is used.

    Parameter punc: a flag, =1 then include punctuations
    """
    input= input.split(" ") # get the tokens
    output={}
    input_nopunc=[]
    if (punc==False):
        for element in input:
            if (element not in string.punctuation): # we hence only exclude total punctuations
                input_nopunc.append(element.replace('\n','')) # This is to remove lines in text
    else:
        for element in input:
            input_nopunc.append(element.replace('\n',''))

    for i in range(len(input_nopunc)-n+1):
        g=' '.join(input_nopunc[i:i+n]) # to form n-gram tokens
        output.setdefault(g, 0) # initiate the dictionary, if not appearing before, set value 0
        output[g] += 1 # count how many time n-gram tokens appears
    return output

def unknown(str, dic, k):
    """
    Returns: a new word string replaces all the words appearing less than k time as
    <unk> token and count the total times of <unk>.

    Run a loop, for all index in the original dictioanry with value<=k will be counted
    into <unk> in the new dictioanry

    parameter str: original string
    Parameter dic: original dictioanry as reference
    Parameter k: threshold for <unk>
    """
    input= str.split(" ") # get the tokens
    input_nopunc=[]
    output=[]
    for element in input:
        if (element not in string.punctuation): # we hence only exclude total punctuations
            input_nopunc.append(element.replace('\n','')) # This is to remove lines in text
    for key in input_nopunc:
        if (key not in dic):
            output.append("<unk>")
        else:
            if ((dic[key]<=k)):
                output.append("<unk>")
            else:
                output.append(key)
    g=" ".join(output)
    return g

def save_model(newdic, file):
    """
    Returns: generate a file containing file information.
    """
    fileName = file+ ".json"
    with open(fileName, 'w') as fp:
        json.dump(newdic, fp)

def bismooth(dic1, dic2, k):
    """
    Returns: a smoothed dictionary containg all the probabilities for words appearing in
    the trained corpus.

    Note this method only works for unseen words, like words appearing
    in unigrams but not bigrams. But it could not help to handle unknown words, i.e. words
    we never even know their existence.
    Basic idea here is to try all possible combinations of unigrams and attach them
    values even if they do not show up.

    Parameter dic1: trained n-gram dictionary
    Parameter dic2: trained 1-gram dictionary
    parameter k: smoothing constant

    """
    output={}
    number= len(dic2)
    for key1 in dic2:
        for key2 in dic2: # Bigrams, hence loop twice
            entry=key1 +' '+ key2
            output.setdefault(entry, k/(number+ dic2[key1])) # add one for all bigrams
            if entry in dic1: # if appearing as bigrams, add up original counts
                output[entry] += (dic1[entry])/(number+ dic2[key1])
    return output


def generator(input, dicn, dic1, n):
    """
    Returns: a word according to probability

    For example, we receive input "I" and using bigram model to predict the next word,
    according to P(word|i).

    Parameter input: a given known string
    Parameter dicn: basically an smoothed probability table
    Parameter dic1: an unigram probability table (after removing all unknown words)
    parameter n: n-gram model we use here
    """
    condition= input[-n:]
    newdic={}
    prob=0
    rand= numpy.random.random()
    for element in condition:
        condition_mod += " "
        if (element in dic1): # which means it is a knwon word
            condition_mod= element
        else:
            condition_mod= "<unk>"
    for key in dic1:
        if (key != "<unk>"):
            p_unk= dicn[condition_mod+ "<unk>"] # This step removes <unk> probability from mass
            prob += dicn[condition_mod+ key]/(1-p_unk) # because we cannot generate an unknown word
            if (prob>rand):
                return key
            break


def perplexity(dictest, dicuse):
    """
    return: perplexity index of a corpula

    Formula: a =+ -math.log(dic["words"])
             exp( 1/tokens* a )

    Parameter dictest: corpula to calculate
    Parameter dicuse: dictionary storing the value of probability
    """
    a=0
    tokens=0
    for key in dictest:
        if key in dicuse:
            a += dictest[key]* math.log(dicuse[key])
            tokens += dictest[key]
        else:
            print(key+'\n')
    output= math.exp(1/tokens * (-a) )
    return output


def train(txt1, txt2, k, n=1):
    """
    return: a trained unigram dictionary.

    Merge the steps from raw data to collected dictionary.
    parameter txt1: raw data (training)
    parameter txt2: raw data (development)
    parameter k: test bi/unigram
    parameter n: smoothing parameter/ hyper parameter
    """
    name=txt1
    txt1=r"C:\Users/13695\Documents\Nature_language_processing/a1/"+txt1+".txt"
    txt2=r"C:\Users/13695\Documents\Nature_language_processing/a1/"+txt2+".txt"
    with open(txt1, 'r', encoding='utf-8') as file1:
        str1= file1.read()
    with open(txt2, 'r', encoding='utf-8') as file2:
        str2= file2.read()
    # First leaning
    dict_uni= ngrammodel.ngrams(str1, 1, 0)
    # Replace unknown in original sentence
    new_str= ngrammodel.unknown(str1, dict_uni, 1)
    test_str= ngrammodel.unknown(str2, dict_uni, 1)
    # Learn n-gram again using unknown
        # training learining
    dict_uni_unk= ngrammodel.ngrams(new_str, 1, 0)
    dict_bi_unk= ngrammodel.ngrams(new_str, 2, 0)
        # testing learning
    dict_uni_unk_test= ngrammodel.ngrams(test_str, 1, 0)
    dict_bi_unk_test= ngrammodel.ngrams(test_str, 2, 0)
        # training smoothing
    dict_bi_smooth= ngrammodel.bismooth(dict_bi_unk, dict_uni_unk, n)

    ngrammodel.save_model(dict_uni, "dic_uni_known_"+ name[-5:])
    ngrammodel.save_model(dict_uni_unk, "dic_uni_unknown_"+ name[-5:])
    #ngrammodel.save_model(dict_bi_unk, "dic_bi_unknown_"+ name[-5:])
    #ngrammodel.save_model(dict_bi_smooth, "dic_bi_unknown_smooth_"+ name[-5:])


    if (k==2):
    # Perplexity testing: bigram
        perplexity= ngrammodel.perplexity(dict_bi_unk_test, dict_bi_smooth)
    # Perplexity testing: unigram
    else:
        perplexity= ngrammodel.perplexity(dict_uni_unk_test, dict_uni_unk)
    return perplexity
