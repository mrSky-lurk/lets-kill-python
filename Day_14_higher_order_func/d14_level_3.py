# Exercises: Level 3
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population
# ================================================================================================================
from data_util import countries_data

print("By Name:: ", sorted(countries_data.country_data, key=lambda item: item['name']))
print("By Capital:: ", sorted(filter(lambda data: data['capital'] != '', countries_data.country_data),
                              key=lambda item: item['capital']))
print("By Population::", sorted(countries_data.country_data, key=lambda item: item['population'], reverse=True))

# Sort out the ten most spoken languages by location.
from collections import Counter
lang_list = [lang for country in countries_data.country_data for lang in country['languages']]
top_lang = sorted(dict(Counter(lang_list)).items(), key=lambda x:x[1])
print("EXTRAORDINARY:: ",top_lang[:5])

# print(countries_sorted_by('population')[0:4])

# Sort out the ten most populated countries.
print("Top 5 Population::", sorted(countries_data.country_data, key=lambda item: item['population'], reverse=True)[:10])



