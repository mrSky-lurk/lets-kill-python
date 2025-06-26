# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
# ================================================================================================================
num=0
print("While loop-")
while num <11:
    print(num, end=' ')
    num += 1
print("\nFor loop-")
for i in range(11):
    print(i, end=' ')

# Iterate 10 to 0 using for loop, do the same using while loop.
# ================================================================================================================
num=10
print("\nWhile loop-")
while num >= 0:
    print(num, end=' ')
    num -= 1
print("\nFor loop-")
num=10
for i in range(11):
    print(num, end=' ')
    num -= 1
print("\nFor loop part 2-")
for i in range(10, 0, -1):
    print(i, end=' ')
print('')
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######
# ================================================================================================================
for row in range(7):
    for col in range(row+1):
        print("*",end='')
    print('')


# Use nested loops to create the following:
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# ================================================================================================================
for row in range(8):
    for col in range(9):
        print("*", end=' ')
    print('')

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
# ================================================================================================================
for num in range(11):
    print("{} x {} = {}".format(num, num, num*num))

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
# ================================================================================================================
py_lib = ['Python', 'Numpy','Pandas','Django', 'Flask']
for lib in py_lib:
    print(lib)

# Use for loop to iterate from 0 to 100 and print only even numbers
# ================================================================================================================
for even in range(0,101, 2):
    print(even, end=' ')
print("")

# Use for loop to iterate from 0 to 100 and print only odd numbers
# ================================================================================================================
for even in range(1,100, 2):
    print(even, end=' ')
print('')