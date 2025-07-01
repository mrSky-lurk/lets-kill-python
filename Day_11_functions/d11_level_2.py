# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.
# ================================================================================================================
import math


def evens_and_odds(num_range):
    even = 0
    odd = 0
    for num in range(num_range + 1):
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    print("The number of evens are:: ", even)
    print("The number of odds are:: ", odd)


evens_and_odds(100)


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print("Factorial of 5 is-")
print(factorial(5))


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
# ================================================================================================================
def is_empty(any):
    if any == None or len(any) == 0:
        print("its empty")
    else:
        print("its not empty")


is_empty('')


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode,
# calculate_range, calculate_variance, calculate_std (standard deviation).
# ================================================================================================================# ================================================================================================================
def calculate_mean(num_list):
    print("Mean:: ", sum(num_list) / len(num_list))


def calculate_median(num_list: list):
    num_list.sort()
    mid = 0
    if len(num_list) % 2 == 0:
        mid = (num_list[int(len(num_list) / 2)] + num_list[int(len(num_list) / 2) - 1]) / 2
    else:
        mid = num_list[int(len(num_list) / 2)]
    print("Median:: ", mid)


from collections import Counter


def calculate_mode(num_list: list):
    counter_map = dict(Counter(num_list))
    counter_map = sorted(counter_map.items(), key=lambda item: item[1], reverse=True)
    print(counter_map)
    mode = list()
    if counter_map[0][1] > 1:
        temp = counter_map[0][1]
        mode.append(counter_map[0][0])
        for index in range(1, len(counter_map)):
            if counter_map[index][1] == temp:
                mode.append(counter_map[index][0])
            else:
                break
    print("Mode: ", mode)


def calculate_range(num_list: list):
    num_list.sort()
    print("Range:: ", num_list[len(num_list) - 1] - num_list[0])


import statistics


def calculate_varience(num_list: list):
    print("Varience::", statistics.variance(num_list))
    return statistics.variance(num_list)


def calculate_std_deviation(num_list: list):
    print("Std Deviation::", math.sqrt((calculate_varience(num_list))))


calculate_mean([2, 4, 6, 8, 10])
calculate_median([2, 4, 6, 8, 10, 12])
calculate_mode([2, 4, 6, 8, 12, 12, 6, 6, 12, 8, 8])
calculate_varience([2, 4, 6, 8, 10, 12])
calculate_std_deviation([2, 4, 6, 8, 10, 12])
