# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
# ================================================================================================================
def isPrime(number):
    if number < 1:
        return False
    else:
        for num in range(2, number):
            if number % num == 0:
                return False
    return True


# print(isPrime(int(input("Enter number to check if its Prime: "))))
print(isPrime(89))

# Write a functions which checks if all items are unique in the list.
# ================================================================================================================
from collections import Counter


def check_unique(any_list):
    item_map = dict(Counter(any_list))
    print(item_map)
    for key, value in item_map.items():
        if value > 1:
            print(key, "has duplicates.")


check_unique([3, 8, 9, 10, 67, 89, 'aloo', 'potol', 'doi', 89, 'lolly', 'aloo'])


# Write a function which checks if all the items of the list are of the same data type.
# ================================================================================================================
def check_datatype(any_list: list):
    expected = type(any_list[0])
    for item in any_list:
        if type(item) != expected:
            print("All members are not of same datatype")
            return
    print("All members are of same",expected)


check_datatype(['aloo', 'potol', 'doi', 'lolly', 'aloo'])

# Write a function which check if provided variable is a valid python variable
# ================================================================================================================
import keyword
def is_validVariable(var):
    if not isinstance(var, str):
        return False
    elif not var.isidentifier():
        return False
    elif keyword.iskeyword(var):
        return False
    return True


print(is_validVariable("Hi12"))
print(is_validVariable("class"))
print(is_validVariable("obj"))
print(is_validVariable("elif"))
print(is_validVariable("break"))
print(is_validVariable(123))


# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order
# ================================================================================================================# ================================================================================================================
from data_util import countries_data
from collections import Counter
def most_spoken_lang(topper:int):
    all_language = list()
    for country in countries_data.country_data:
        for lang in country.get('languages'):
            all_language.append(lang)
    lang_map = dict(Counter(all_language))
    lang_map_sorted = dict(sorted(lang_map.items(), key=lambda item:item[1], reverse=True))
    # print(lang_map_sorted)
    # print(lang_map_sorted[0][1])
    next_lang = iter(lang_map_sorted)
    for index in range(topper):
        key = next(next_lang, None)
        if key is None:
            print("end of list")
            break
        print(key, "->", lang_map_sorted.get(key))


most_spoken_lang(10)


# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
# ================================================================================================================
def most_populated_countries(topper:int):
    population_map = dict()
    for country in countries_data.country_data:
        population_map[country.get('name')] = country.get('population')
    # print(population_map)
    sorted_population_map = dict(sorted(population_map.items(), key=lambda item: item[1], reverse=True))
    itr = iter(sorted_population_map)
    for index in range(topper):
        key = next(itr, None)
        if key is None:
            print("End of list")
            break
        print("Rank {}: {} with population of  {}".format(index+1, key, sorted_population_map.get(key)))


most_populated_countries(20)


