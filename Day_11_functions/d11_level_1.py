# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
# ================================================================================================================
import math


def add_nums(num_1, num_2):
    return num_1 + num_2


print(add_nums(4, 10))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
# ================================================================================================================
def area_circle(radius, pi=3.14):
    return pi * radius ** 2


print("Area of Circle with radius 5:: ", area_circle(5))


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
# ================================================================================================================# ================================================================================================================
def sum_all(*num_list):
    sum_value = 0.0
    for num in num_list:
        if type(num) == int or type(num) == float:
            sum_value = sum_value + num
        else:
            print("this is not an int or float - ", num)
    return sum_value


print(sum_all(7, 10, '3', 1))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
# ================================================================================================================
def celsius_to_fahrenheit(temp_in_c):
    return (temp_in_c * 9 / 5) + 32


print("40°C to fahrenheit -> ", celsius_to_fahrenheit(40))


# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
# ================================================================================================================
def get_season(month):
    autumn_month = {'September', 'October', 'November'}
    winter_month = {'December', 'January', 'February'}
    summer_month = {'June', 'July', 'August'}
    spring_month = {'March', 'April', 'May'}
    if month in autumn_month:
        print("Autumn")
    elif month in winter_month:
        print("Winter")
    elif month in spring_month:
        print("Spring")
    elif month in summer_month:
        print("Summer")


get_season('April')


# Write a function called calculate_slope which return the slope of a linear equation
# ================================================================================================================
def calculate_slope(point_a, point_b, c=0):
    x1_axis = point_a[0]
    y1_axis = point_a[1]
    x2_axis = point_b[0]
    y2_axis = point_b[1]
    slope = ((y2_axis - y1_axis) - c) / (x2_axis - x1_axis)  # y = mx + c; m is slope
    return slope


print("slope of the st.line connecting (2,6) & (5,4):: ", calculate_slope((2, 6), (5, 4)))


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# ================================================================================================================# ================================================================================================================
def solve_quadratic_eqn(a, b, c):
    discrim = math.sqrt((b ** 2) - (4 * a * c))
    sol1 = (-b + discrim) / 2 * a
    sol2 = (-b - discrim) / 2 * a
    return sol1, sol2


print("Roots::: ", solve_quadratic_eqn(1, -3, 2))


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
# ================================================================================================================
def print_list(any_list):
    for item in any_list:
        print(item.title(), end=', ')


print(print_list(['india', 'england', 'arab', 'africa']))


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# ================================================================================================================
def reverse_list(any_list):
    r_list = list()
    for index in range((len(any_list)) - 1, -1, -1):
        r_list.append(any_list[index])
    return r_list


print("Reverse list of [10,70,80,50,90]")
print(reverse_list([10, 70, 80, 50, 90]))


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
# ================================================================================================================
def capitalize_list_items(any_list):
    index = 0
    for item in any_list:
        any_list[index] = item.upper()
        index += 1
    return any_list


print("capitaize this list- [bird, Hola, Pinnacle, Instamart, lolly]")
print(capitalize_list_items(['bird', 'Hola123', 'Pinnacle', 'Instamart', 'lolly']))


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
# numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
# ================================================================================================================
def update_the_list(any_list, new_item):
    print("Old List - ", any_list)
    any_list.append(new_item)
    return any_list


print(update_the_list([2, 3, 7, 9], 5))


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]
# ================================================================================================================
def remove_item(any_list, removed_item):
    print("Old list-", any_list)
    print("Removed- ", removed_item)
    any_list.remove(removed_item)
    return any_list


print(remove_item(['Potato', 'Tomato', 'Mango', 'Milk'], 'Mango'))


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
# ================================================================================================================
def sum_of_numbers(num_range):
    sum = 0
    print("Adding all number 1 to", num_range)
    for num in range(num_range + 1):
        sum += num
    return sum


print(sum_of_numbers(10))


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
# ================================================================================================================
def add_all_odds(num_range):
    sum = 0
    print("Adding all Odds in the range 1 to", num_range)
    for num in range(num_range + 1):
        if num % 2 != 0:
            print(num)
            sum += num
    print('-----------------')
    return sum


print(add_all_odds(10))


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def add_all_even(num_range):
    sum = 0
    print("Adding all Evens in the range 1 to", num_range)
    for num in range(num_range + 1):
        if num % 2 == 0:
            print(num)
            sum += num
    print('-----------------')
    return sum


print(add_all_even(10))
