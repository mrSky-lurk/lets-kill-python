# Filter only negative and zero in the list using list comprehension
# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# ================================================================================================================
from typing import List, Tuple

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_nums = [num for num in numbers if num <= 0]
print(negative_nums)

# Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ================================================================================================================
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]  # [list_of_list[list2[final_list[elm]]]]
# list_2 = [elm for elm in list_of_lists if type(elm) == list ]
flat_list = [elm for list2 in list_of_lists for final_list in list2 for elm in final_list]
print("flat list:: ", flat_list)

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# ================================================================================================================
# for row in range(11):
#     row_list = [row, 1]
#     for col in range(1, 6):
#         new_entry = row ** col
#         row_list.append(new_entry)
#     row_tuple = tuple(row_list)
#     multiply_num_list.append(row_tuple)
# print(abc)
# abc = [[row]+[1]+[row**col for col in range(1,6)] for row in range(11)]
multiply_num_list = [tuple([row] + [1] + [row ** col for col in range(1, 6)]) for row in range(11)]
print(multiply_num_list)


# Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
# ================================================================================================================
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# new_list_1 = [country_cap for country_inner_list in countries for country_tup in country_inner_list for country_cap in country_tup]
new_list = [[country_tup[0],country_tup[0].upper()[0:3],country_tup[1]] for country_inner_list in countries for country_tup in country_inner_list]
print(new_list)

# Change the following list to a list of dictionaries:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
# ================================================================================================================
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list = [{'country':country_tuple[0].upper(),'capital':country_tuple[1].upper()} for country_inn_list in countries for country_tuple in country_inn_list]
print(dict_list)

# Change the following list of lists to a list of concatenated strings:
# names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
# ================================================================================================================
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
list_names = [name_tup[0] + " " + name_tup[1] for inner_list in names for name_tup in inner_list]
print(list_names)


# Write a lambda function which can solve a slope or y-intercept of linear functions.
# ================================================================================================================
m = lambda x1,x2,y1,y2,c=0: (y2-y1)/(x2-x1) - c if x2-x1 != 0 else float('inf')