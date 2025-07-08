# Exercises: Level 2
from functools import reduce

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
# ================================================================================================================
new_country = map(lambda name: name.upper(), countries)
print(list(new_country))

# Use map to create a new list by changing each number to its square in the numbers list
# ================================================================================================================
square_list = map(lambda num: num ** 2, numbers)
print(list(square_list))

# Use map to change each name to uppercase in the names list
# ================================================================================================================
name_upper = map(lambda name: name.upper(), names)
print(list(name_upper))


# Use filter to filter out countries containing 'land'.
# ================================================================================================================
def only_land(country):
    if "land" in country:
        return True
    return False


land_country = filter(only_land, countries)
print(list(land_country))


# Use filter to filter out countries having exactly six characters.
# ================================================================================================================
def six_char_country(country):
    if len(country) == 6:
        return True
    return False


print(list(filter(six_char_country, countries)))


# Use filter to filter out countries containing six letters and more in the country list.
# ================================================================================================================
def six_or_more_char_country(x):
    if len(x) >= 6:
        return True
    return False


print(list(filter(six_or_more_char_country, countries)))


# Use filter to filter out countries starting with an 'E'
# ================================================================================================================
def statrs_with_E(x):
    if x.startswith('E'):
        return True
    return False


print(list(filter(statrs_with_E, countries)))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
# ================================================================================================================
print(reduce(lambda a, b: a + b,
             filter(lambda x: x > 50,
                    map(lambda num: num ** 2, numbers))))
print(64 + 81 + 100)


# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
# ================================================================================================================
def list_to_string(any_list):
    def convert():
        print(list(map(lambda item: str(item), any_list)))

    return convert


list_to_string(numbers)()

# Use reduce to sum all the numbers in the numbers list.
# ================================================================================================================
print(reduce(lambda a, b: a + b, numbers))


# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# ================================================================================================================
def join_countries(x, y):
    delimiter = ' and ' if y == 'Iceland' else ', '
    return x + delimiter + y


print(f"{reduce(lambda a, b: str(a + ',' + b), countries)} are north European countries")
print(f"{reduce(join_countries, countries)} are north European countries")

# Declare a function called categorize_countries that returns a list of countries with some common pattern
# (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
# ================================================================================================================
from data_util import country_list


def filter_with_pattern(pattern):
    def filter_country_stan(country):
        return True if pattern in country else False

    return filter_country_stan


def categorize_countries(pattern):
    filtered_list = filter(filter_with_pattern(pattern), country_list.countries)
    print(list(filtered_list))


print(filter_with_pattern('stan')('pakistan'))
categorize_countries('stan')
categorize_countries('land')
categorize_countries('ia')

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
# ================================================================================================================

country_sorted_dict = dict()


def filter_countries_startswith(starts_with):
    def check_condition(country: str):
        return country.upper().startswith(starts_with.upper())

    return check_condition


for country in country_list.countries:
    if country[0] not in country_sorted_dict.keys():
        temp_list = list(filter(filter_countries_startswith(country[0]), country_list.countries))
        country_sorted_dict[country[0]] = temp_list

print(country_sorted_dict)

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# ================================================================================================================
# first_ten = [country for index, country in enumerate(country_list.countries) if index < 10]
# or
first_ten = list(country_list.countries[0:10])
print(first_ten)


# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(any_list):
    last_ten = any_list[-10:]
    return last_ten


print(get_last_ten_countries(country_list.countries))
