"""
Unit test for module ngrammodel

When run as a script, this module invokes several procedures that
test the various functions in the module ngrammodel.

Author: Tianli Xia
Date:   Sep 12th, 2018
"""

import ngrammodel
import introcs
import string

def testA():
    """
    test for ngrams functions.
    """
    print("Test the ngrams functions.")
    input="aa bb cc dd bb aa cc bb"
    output=ngrammodel.ngrams(input, 2)
    print(output)


def testB():
    """
    test for preprocessed functions.
    """
    print("Test the preprocessed functions.")
    input="I went to the school, and didn't see any one."
    output="i went to the school and didn't see any one"
    print(ngrammodel.prep(input, 1))
    introcs.assert_equals(ngrammodel.prep(input, 1), output)


testA()
testB()

print("Please see the return value to determine if this runs correctly.")
