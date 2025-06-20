# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
# ================================================================================================================
score = float(input("What is your score out of 100:: "))
if score >= 80:
    print("Your Grade is 'A'")
elif score >= 70:
    print("Your Grade is 'B'")
elif score >=60:
    print("Your Grade is 'C'")
elif score >= 50:
    print("Your Grade is 'D'")
else:
    print("You have FAILED")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# ================================================================================================================# ================================================================================================================
autumn_month = {'September', 'October', 'November'}
winter_month = {'December', 'January', 'February'}
summer_month = {'June', 'July', 'August'}
spring_month = {'March', 'April', 'May'}
month = input("Enter month to find out season:: ").title()
if month in autumn_month:
    print("Autumn")
elif month in winter_month:
    print("Winter")
elif month in spring_month:
    print("Spring")
elif month in summer_month:
    print("Summer")


# The following list contains some fruits:
# fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
# ================================================================================================================
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a new fruit:: ").lower()
if new_fruit in fruits:
    print("{} already exists in the list.".format(new_fruit))
else:
    fruits.append(new_fruit)
    print("{} added successfully to the list.".format(new_fruit))
    print("Updated list:: ", fruits)