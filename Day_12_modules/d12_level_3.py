# Exercises: Level 3
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
# ================================================================================================================
import random


def shuffle_list(any_list:list):
    shuffled_list = list()
    item_count = len(any_list)
    for index in range(item_count):
        discard_item = random.choice(any_list)
        shuffled_list.append(discard_item)
        any_list.remove(discard_item)
    return shuffled_list

my_list = ['tobacco', 'steel', 'mango', 'eye', 'belly', 'kite']
print(shuffle_list(my_list))


# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique
# ================================================================================================================
import string

def array_of_unique_digits(length:int):
    digit_set = list(string.digits)
    num_list=  list()
    for index in range(length):
        discard_digit = random.choice(digit_set)
        num_list.append(discard_digit)
        digit_set.remove(discard_digit)
        if not digit_set:
            num_list.append("Ran out of unique digits...")
            break
    return num_list

print(array_of_unique_digits(11))
