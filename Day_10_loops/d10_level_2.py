# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# O/P:: 5050.
# ================================================================================================================
sum = 0
for num in range(101):
    sum = sum + num
else:
    print("Total:: ", sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
# ================================================================================================================
evn_total = 0
odd_total = 0
for i in range(101):
    if i % 2 == 0:
        evn_total = evn_total + i
    else:
        odd_total = odd_total + i
print("Total of all Even: ", evn_total)
print("Total of all Odd: ", odd_total)

# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
