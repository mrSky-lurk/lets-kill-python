# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# ================================================================================================================
from data_util import country_list
from data_util import countries_data
for country in country_list.countries:
    if 'land' in country:
        print(country)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# ================================================================================================================
fruits = ['banana', 'orange', 'mango', 'lemon']
total = len(fruits)
new_list=[]
for index in range(total-1, -1, -1):
    new_list.append(fruits[index])
print("new list:: ",new_list)

# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# ================================================================================================================
all_languages = set()
for country in countries_data.country_data:
    # print(country.get('languages'))
    # break
    all_languages.update(country.get('languages'))
print("All languages:: ",all_languages)
print("Total languages:: ",len(all_languages))


# Find the ten most spoken languages from the data
# ================================================================================================================
lang_map = dict()
for country in countries_data.country_data:
    get_lang_list = country.get('languages')
    # print(get_lang_list)
    for lang in get_lang_list:
        if lang in lang_map.keys():
            value = lang_map.get(lang) + 1
        else:
            value = 1
        lang_map[lang] = value
print("Usage of all languages: ",lang_map)
sorted_lang_map = dict(sorted(lang_map.items(), key=lambda item:item[1]))
most_used = next(reversed(sorted_lang_map))
print("sorted ascending:: ",sorted_lang_map)
print("most used language is {} and its used by {} regions.".format(most_used, sorted_lang_map.get(most_used)))
print("Top 10 most spoken languages in descending order - ")
lang_map_key = reversed(sorted_lang_map)
for count in range(1,11):
    key = next(lang_map_key)
    print("{} -> {} spoken by {} regions.".format(count, key, sorted_lang_map[key]))

# Find the 10 most populated countries in the world
population_map = dict()
for country in countries_data.country_data:
    key = country.get("name")
    value = country.get('population')
    population_map[key]=value
sorted_population_map = dict(sorted(population_map.items(), key=lambda item:item[1], reverse=True))
print(sorted_population_map)
print("Top 10 most populated Countries:")
itr = iter(sorted_population_map)
for i in range(1,11):
    key = next(itr)
    print("{} with population {}".format(key, sorted_population_map.get(key)))


