# ### Exercises: Level 1

# 1. Write a function which generates a six digit/character random_user_id.
#      print(random_user_id());
#      '1ee33d'
# ================================================================================================================
from random import *
import string


def random_user_id(length: int):
    user_id = ''
    for i in range(length):
        user_id = user_id + choice(string.ascii_lowercase.join(string.digits))
    return user_id


print(random_user_id(9))


# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf
# ================================================================================================================

def generate_id_of_length(length):
    user_id = ''
    for i in range(length):
        user_id = user_id + (choice(string.ascii_letters+string.digits))
    return user_id

def user_id_gen_by_user():
    length = int(input("Enter the length of user id:: "))
    num_of_id_needed = int(input("Enter the total number of user id required:: "))
    final_id=list()
    for count in range(num_of_id_needed):
        final_id.append(generate_id_of_length(length))
    return '\n'.join(final_id)


# print(user_id_gen_by_user())

# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form
# ================================================================================================================
def rgb_color_gen():
    rgb_final = list()
    for i in range(3):
      rgb_final.append(f"{randint(0, 255):03d}")
    return "rgb({})".format(",".join(rgb_final))

print(rgb_color_gen())