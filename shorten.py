import underthesea as uds
import re
import numpy as np


def get_sentence_score(sent):
    score_map = {
        'gen': 1,
        'bạn': 2,
        'không': 1,
        'khuyên': 2
    }
    words = re.findall(r'\w+', sent.lower())
    score = 0
    for word in words:
        if word in score_map.keys():
            score += score_map[word]
    return score


def shorten(text, num_sents=1):
    scores = []
    paragraphs = text.split('\n')
    sents = []
    for par in paragraphs:
        sents += uds.sent_tokenize(par)
    for sent in sents:
        scores.append(get_sentence_score(sent))
    idxs = sorted(np.argsort(scores)[-num_sents:])
    return '\n'.join(sents[i] for i in idxs)