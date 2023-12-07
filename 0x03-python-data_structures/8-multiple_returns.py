#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return ((0, None))
    else:
        for c in sentence:
            return ((len(sentence), c))
