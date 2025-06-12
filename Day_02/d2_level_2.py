import math

import d2_level_1

add_new = input('Do you want to Add new details:\n')

full_name = ex_level_1.full_name
age = ex_level_1.age
first_name = ex_level_1.first_name
last_name = ex_level_1.last_name
if  add_new.upper() != 'NO':
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    full_name = first_name+' '+last_name
    age = int(input('Enter Age: '))
    print('New Details::')
else:
    print('Existing Details::')
print(full_name)
print(len(full_name))
print(type(age))
print(len(first_name) - len(last_name))

num_one = 80
num_two = 5
total = num_one + num_two
print(total)
diff = num_one - num_two
print(diff)
multiply = num_two * num_one
print(multiply)
div = num_one / num_two
print(div)
exp = num_two ** num_one
print(exp)
floor = num_one // num_two
print(floor)
print(math.pi)

# Work with Circles
radius = float(input('Enter the radius of a circle:\n'))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius
print('Area of the circle is: ', area_of_circle)
print('Circumference of the circle is: ', circum_of_circle)




