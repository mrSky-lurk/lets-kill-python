# Exercises: Level 1
# Create an empty tuple
# ================================================================================================================
empty_tuple = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
# ================================================================================================================
bros = ('Jon', 'Rob', 'Theon')
sisters = ('Arya', 'Sansa')

# Join brothers and sisters tuples and assign it to siblings
# ================================================================================================================
siblings = bros + sisters
print(siblings)

# How many siblings do you have?
# ================================================================================================================
print("Number of siblings:: ", len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
# ================================================================================================================
siblings_list = list(siblings)
siblings_list.append('Ned')
siblings_list.append('Catlyn')
print("sibling and mom dad:: ",siblings_list)
family = tuple(siblings_list)
print("Family members:: ", family)

