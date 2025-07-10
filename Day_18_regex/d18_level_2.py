# Exercises: Level 2
# Write a pattern which identifies if a string is a valid python variable
# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True
# ================================================================================================================

import re
import keyword

def is_valid_variable(var):
    regex_pattern = r'^[a-z][A-Za-z0-9_]*$'
    return True if re.match(regex_pattern, var) != None and not keyword.iskeyword(var) else False

print(is_valid_variable("if")) # False
print(is_valid_variable("await")) # False
print(is_valid_variable("iF")) # True
print(is_valid_variable("i_am_*&^")) # FALSE
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True