#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        c = len(sentence), None
    else:
        c = len(sentence), sentence[0]
    return c
