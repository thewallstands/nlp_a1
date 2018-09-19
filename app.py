"""
User interface for module ngrammodel

When run as a script, this module calculates the n-gram model and execute the
things we want to do.

Author: Tianli Xia
Date:   Sep 11th, 2018
"""


import ngrammodel
import string
import io

file_trump_train = (r"C:\Users/13695\Documents\Nature_language_processing/a1/train/trump.txt")
file_obama_train = (r"C:\Users/13695\Documents\Nature_language_processing/a1/train/obama.txt")
file_trump_dev = (r"C:\Users/13695\Documents\Nature_language_processing/a1/development/trump.txt")
file_obama_dev = (r"C:\Users/13695\Documents\Nature_language_processing/a1/development/obama.txt")


k=2 # bigram

result=[]
for txt1,txt2 in [r"train/trump",r"train/obama"],[r"development/trump",r"development/obama" ]:
    name= txt1[-5:]
    txt1=r"C:\Users/13695\Documents\Nature_language_processing/a1/"+txt1+".txt"
    txt2=r"C:\Users/13695\Documents\Nature_language_processing/a1/"+txt2+".txt"

    with io.open(txt1, 'r', encoding='utf-8') as file1:
        str1= file1.read()
    with io.open(txt2, 'r', encoding='utf-8') as file2:
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
    ngrammodel.save_model(dict_uni, "dic_uni_known_"+ name[-5:])
    ngrammodel.save_model(dict_uni_unk, "dic_uni_unknown_"+ name[-5:])

    perplexity=[]
    for n in range(200):
        n=(n+1)/100
        # training smoothing
        dict_bi_smooth= ngrammodel.bismooth(dict_bi_unk, dict_uni_unk, n)

    #ngrammodel.save_model(dict_bi_unk, "dic_bi_unknown_"+ name[-5:])
    #ngrammodel.save_model(dict_bi_smooth, "dic_bi_unknown_smooth_"+ name[-5:])

        if (k==2):
    # Perplexity testing: bigram
            perplexity.append(ngrammodel.perplexity(dict_bi_unk_test, dict_bi_smooth))
            print(str(perplexity[-1]))
    # Perplexity testing: unigram
        else:
            perplexity.append(ngrammodel.perplexity(dict_uni_unk_test, dict_uni_unk))
    #    return perplexity
    result.append(perplexity)
ngrammodel.save_model(result, result)
#perplexity_trump=ngrammodel.train(r"train/trump",r"development/trump",2)
#perplexity_obama=ngrammodel.train(r"train/obama",r"development/obama",2)
