# Exercises: Level 3
# Clean the following text. After cleaning, count three most frequent words in the string.
# print(clean_text(sentence));
# ================================================================================================================
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

import re
def clean_text(text):
    patter_regex = r'[^A-Za-z0-9,. ]'
    return re.sub(patter_regex,'',text)

print(clean_text(sentence))


# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
# ================================================================================================================
from collections import Counter

def clean_it_first(function):
    def clean_it():
        func = function()
        filter_regex = r'[^A-Za-z0-9 ]'
        clean_text = re.sub(filter_regex, '', func)
        return clean_text
    return clean_it

@clean_it_first
def return_clean_sentence():
    return sentence

print(return_clean_sentence())


def most_frequent_words(text):
    word_count = dict(Counter(text.split(' ')))
    word_count_sorted = sorted(word_count.items(), key=lambda item:item[1], reverse=True)
    word_count_frequent = dict(filter(lambda item: item[1] > 1, word_count.items()))
    # return word_count_sorted
    return word_count_frequent

print(most_frequent_words(return_clean_sentence()))