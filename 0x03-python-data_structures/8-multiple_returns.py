#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = ()
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    new_tuple = (len(sentence), first_char)
    return new_tuple
