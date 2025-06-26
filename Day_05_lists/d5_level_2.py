# Exercises: Level 2
# The following is a list of 10 students ages:
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
# ================================================================================================================
from data_util import country_list
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
max_age = sorted(ages)[-1]
min_age = sorted(ages)[0]
print("Min age:: ", min_age)
print("Max age:: ", max_age)

# Add the min age and the max age again to the list
# ================================================================================================================
ages.append(min_age)
ages.append(max_age)
print("Added min and max age again to the list:: ", ages)

# Find the median age (one middle item or two middle items divided by two)
# ================================================================================================================
sorted_age = ages.copy()
sorted_age.sort()
print("Sorted ages:: ", sorted_age)
if len(sorted_age) % 2 != 0:
    mean_age = sorted_age[int(len(sorted_age) / 2)]
else:
    mean_age = (sorted_age[int(len(sorted_age) / 2)] + sorted_age[int(len(sorted_age) / 2) - 1]) / 2
print("Mean of all ages:: ", mean_age)

# Find the average age (sum of all items divided by their number )
# ================================================================================================================
average = sum(ages) / len(ages)
print("Average:: ", average)

# Find the range of the ages (max minus min)
# ================================================================================================================
print("Range:: ", max_age - min_age)

# Compare the value of (min - average) and (max - average), use abs() method
print("Comparing the value of (min - average) and (max - average):: ", abs((max_age - average) - (min_age - average)))

# Find the middle country(ies) in the countries list
# ================================================================================================================
country_list.countries.append("Deccan")
len_countrylist = len(country_list.countries)
print(len_countrylist)
if len_countrylist % 2 != 0:
    print("Mid country:: ", country_list.countries[int(len_countrylist / 2)])
else:
    print("Mid Countries:: ", country_list.countries[(int(len_countrylist / 2) - 1):(int(len_countrylist / 2) + 1)])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
# ================================================================================================================
print("Initial length:: ", len(country_list.countries))
if len_countrylist % 2 == 0:
    first_list = country_list.countries[0:int(len_countrylist / 2)]
    print(len(first_list))
    second_list = country_list.countries[int(len_countrylist / 2):]
    print(len(second_list))
else:
    first_list = country_list.countries[0:int(len_countrylist / 2 + 1)]
    print(len(first_list))
    second_list = country_list.countries[int(len_countrylist / 2 + 1):]
    print(len(second_list))

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_three = country_list[0:3]
scandic_country = country_list[3:]
print("First three:: ", first_three)
print("Scandic countries:: ", scandic_country)
