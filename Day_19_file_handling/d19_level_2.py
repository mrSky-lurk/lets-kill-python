# Exercises: Level 2
# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
# ================================================================================================================
from pathlib import Path
import re

path_to_file = Path(__file__).resolve().parents[1]/ "data"/"email_exchanges_big.txt"
with path_to_file.open() as raw_emails:
    content = raw_emails.read()
email_id_list = list()
for email in content.split("From "):
    email_like_str = email.split(' ')[0]
    if bool(re.match(r'^[a-z0-9.]+@[a-z]+\.[a-z]+(\.[a-z])*$', email_like_str)):
        email_id_list.append(email_like_str)
print(email_id_list)
print(len(email_id_list))
print("uniques emails::", len(set(email_id_list)))


# Find the most common words in the English language. Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and a positive integer, indicating the number of words.
# Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]
# ================================================================================================================
from collections import Counter

def find_most_common_words(file_name, top_count, filter_text = False):
    try:
        path_to_file = Path(__file__).resolve().parents[1] / "data" / file_name
        with path_to_file.open() as speech:
            text_part = speech.read()
    except:
        print("Not a file")
        text_part = file_name
    if filter_text:
        text_part = clean_text(text_part)
    word_counter = dict(Counter(text_part.split(" ")))
    word_counter = sorted(word_counter.items(), key=lambda x: x[1], reverse=True)
    rev_map = [(item[1],item[0]) for item in word_counter]
    return rev_map[:top_count]

print(find_most_common_words("sample.txt", 10))
print(find_most_common_words("Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory", 10))

# Use the function, find_most_frequent_words to find:
# a) The ten most frequent words used in Obama's speech
# b) The ten most frequent words used in Michelle's speech
# c) The ten most frequent words used in Trump's speech
# d) The ten most frequent words used in Melina's speech
# ================================================================================================================
print(find_most_common_words("donald_speech.txt", 10))
print(find_most_common_words("obama_speech.txt", 10))
print(find_most_common_words("michelle_obama_speech.txt", 10))
print(find_most_common_words("melina_trump_speech.txt", 10))

# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions,
# function to clean the text(clean_text),
# function to remove support words(remove_support_words)
# and finally to check the similarity(check_text_similarity).
# List of stop words are in the data directory
# ================================================================================================================
from data_util import stop_words
import re
def remove_support_words(func):
    def remove_words(text_item:str):
        text_item = re.sub(r'[^a-zA-Z0-9 \n]', '', text_item)
        filter_text = filter(lambda item: item not in stop_words.stop_words, text_item.replace('\n', ' ').split(' '))
        return func(' '.join(filter_text))
    return remove_words
@remove_support_words
def clean_text(text):
    return text

def return_similar_words(text_1, text_2):
    clean_text_1 = set(clean_text(text_1).split(' '))
    clean_text_2 = set(clean_text(text_2).split(' '))
    similar_words = clean_text_1.intersection(clean_text_2)
    return '\n'.join(similar_words)


from pathlib import Path
def read_file(file_name):
    try:
        path_to_file = Path(__file__).resolve().parents[1] / "data" / file_name
        with path_to_file.open() as file:
            return file.read()
    except:
        print("This is a string")
        return file_name
def check_text_similarity(entry_1, entry_2):
    print(return_similar_words(read_file(entry_1), read_file(entry_2)))

check_text_similarity("my pig is actually a cow and he could vomit a cat",  "the range of cat breeds sacre of his pig can be considered as vomit")
check_text_similarity("melina_trump_speech.txt",  "michelle_obama_speech.txt")
print("# ================================================================================================================")


# Find the 10 most repeated words in the romeo_and_juliet.txt
# ================================================================================================================
print(find_most_common_words("romeo_and_juliet.txt", 10, True))


# Read the hacker news csv file and find out:
# a) Count the number of lines containing python or Python
# b) Count the number lines containing JavaScript, javascript or Javascript
# c) Count the number lines containing Java and not JavaScript
# ================================================================================================================
import csv


def read_csv_count_lines_for_keyword(keyword):
    path_to_file = Path(__file__).resolve().parents[1] / "data" / "hacker_news.csv"
    with path_to_file.open() as file:
        read_csv = csv.reader(file, delimiter=',')
        header_found = False
        line_count_contains_keyword = 0
        for row in read_csv:
            if not header_found:
                print("Columns are: ", ', '.join(row))
                header_found = True
            else:
                if any(re.search(fr'\b{re.escape(keyword)}\b', item, re.IGNORECASE) for item in row):
                    line_count_contains_keyword += 1
    return line_count_contains_keyword



print("hello ===== ",read_csv_count_lines_for_keyword("python"))
