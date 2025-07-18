# Exercises: Level 1
# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words
# ================================================================================================================
from pathlib import Path


def speech_details(file_name):
    path_to_root = Path(__file__).resolve().parents[1]
    with open(path_to_root / "data" / file_name) as speech:
        speech_lines = speech.readlines()
        speech_words = len(speech.read().split(' '))
        print(f"File name:: {file_name}")
        print("================================================")
        print("Number of lines", len(speech_lines))
        print("Total word count", speech_words)
        print("================================================")


speech_details("obama_speech.txt")
speech_details("michelle_obama_speech.txt")
speech_details("donald_speech.txt")
speech_details("melina_trump_speech.txt")

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
#
# # Your output should look like this
# print(most_spoken_languages(filename='./data/countries_data.json', 10))
# [(91, 'English'),
# (45, 'French'),
# (25, 'Arabic'),
# (24, 'Spanish'),
# (9, 'Russian'),
# (9, 'Portuguese'),
# (8, 'Dutch'),
# (7, 'German'),
# (5, 'Chinese'),
# (4, 'Swahili'),
# (4, 'Serbian')]
#
# ================================================================================================================
import json
from collections import Counter


def most_spoken_languages(file_name, entries_from_top):
    data_dict = read_json_file(file_name)
    lang_list = [lang for country in data_dict for lang in country['languages']]
    most_to_least_spoken = sorted(Counter(lang_list).items(), key=lambda x: x[1], reverse=True)
    return [(lang_count[1], lang_count[0]) for lang_count in most_to_least_spoken[:entries_from_top]]


def read_json_file(file_name):
    path_to_root = Path(__file__).resolve().parents[1]
    path_to_file = path_to_root / "data" / file_name
    with open(path_to_file, encoding="utf-8") as data:
        data_dict = json.load(data)
    return data_dict


print(most_spoken_languages("countries_data.json", 9))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
#
# # Your output should look like this
# print(most_populated_countries(filename='./data/countries_data.json', 10))
#
# [
# {'country': 'China', 'population': 1377422166},
# {'country': 'India', 'population': 1295210000},
# {'country': 'United States of America', 'population': 323947000},
# {'country': 'Indonesia', 'population': 258705000},
# {'country': 'Brazil', 'population': 206135893},
# {'country': 'Pakistan', 'population': 194125062},
# {'country': 'Nigeria', 'population': 186988000},
# {'country': 'Bangladesh', 'population': 161006790},
# {'country': 'Russian Federation', 'population': 146599183},
# {'country': 'Japan', 'population': 126960000}
# ]
# ================================================================================================================

def most_populated_countries(file_name, entries):
    path_to_file = Path(__file__).resolve().parents[1] / "data" / file_name
    with path_to_file.open(encoding="utf-8") as all_country:
        country_dct = json.load(all_country)
    country_population = [{'name': country['name'], 'population': country['population']} for country in country_dct]
    top_entries = sorted(country_population, key=lambda x: x['population'], reverse=True)[:entries]
    return top_entries


print(most_populated_countries("countries_data.json",10))