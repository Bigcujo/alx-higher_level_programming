#!/usr/bin/python3
def multiple_returns(sentences):
    if not sentences:
        sentences = None
    if sentences:
        sen_len = len(sentences)
    else:
        sen_len = 0
    return (sen_len, sentences if not sentences else sentences[:1])
