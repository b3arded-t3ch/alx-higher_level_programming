#!/usr/bin/python3
def multiple_returns(sentence):
    sent_length = len(sentence)
    if sent_length == 0:
        return (sent_length, None)
    else:
        return (sent_length, sentence[0])
