import re                               # required for string substitution
import string                           # required for removing punctuation
from collections import defaultdict     # required for creating dictionary

def word_count(filename, lower_case=False, remove_punc=False):
    """Open a file, count the words, and return a dictionary with words as keys and the count of each word as value."""

    word_freq_dic = defaultdict(int)
    data = open('toy.txt').read()

    # removing newline marks from the corpus
    data = re.sub('[\n]', ' ', data).split()

    if lower_case:
        if remove_punc:
            new_data = [word.lower() for word in data if word not in string.punctuation]
        else:
            new_data = [word.lower() for word in data]
    else:
        if remove_punc:
            new_data = [word for word in data if word not in string.punctuation]
        else:
            new_data = [word for word in data]

    for word in new_data:
        if word in word_freq_dic.keys():
            word_freq_dic[word] += 1
        else:
            word_freq_dic[word] = 1

    return word_freq_dic

#c = word_count('toy.txt')
#print(c['And'])









    


