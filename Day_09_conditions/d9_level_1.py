# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
# ================================================================================================================
your_age = int(input("Enter your age:: "))
if your_age >= 18:
    print("U are old enough to drive")
else:
    print("U are NOT old enough to drive. You have to wait for {} more year(s)!".format(18 - your_age))

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# ================================================================================================================
# Enter your age: 30
# You are 5 years older than me.
# ================================================================================================================
my_age = 30
if your_age > my_age:
    print("You are older than me by {} {}".format(your_age - my_age,'years.' if abs(your_age - my_age) > 1 else 'year.'))
elif your_age == my_age:
    print("You and me can be friends!")
else:
    print("You are younger than me by {} {}".format(my_age - your_age,'years.' if abs(your_age - my_age) > 1 else 'year.'))

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
# ================================================================================================================
# same as above