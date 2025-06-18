# Exercises: Level 2
# Unpack siblings and parents from family_members
# ================================================================================================================
family = ('Jon', 'Rob', 'Theon', 'Arya', 'Sansa', 'Ned', 'Catlyn')
print("Stark Siblings:: ", family[0:-2])
print("Stark Parents:: ", family[-2:])

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
# ================================================================================================================
fruits = ('banana', 'orange', 'mango', 'lemon')
veggies = ('Potato', 'tomato', 'beans', 'onion')
proteins = ('Chicken', 'Mutton', 'Paneer', 'Fish')
food_stuff_tp = fruits+veggies+proteins
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
# ================================================================================================================
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
# ================================================================================================================
if len(food_stuff_lt) % 2 != 0:
    mid_index = int(len(food_stuff_lt) / 2)
    print("Middle item:: ", food_stuff_lt[mid_index])
else:
    mid_1 = int(len(food_stuff_lt) /2 -1)
    mid_2 = int(len(food_stuff_lt) /2)
    print("Middle items:: {} & {}".format(food_stuff_lt[mid_1], food_stuff_lt[mid_2]))

# Slice out the first three items and the last three items from food_staff_lt list
# ================================================================================================================
print("First three:: ", food_stuff_lt[0:3])
print("Last three:: ", food_stuff_lt[-3:])
# Delete the food_staff_tp tuple completely
del food_stuff_lt

# Check if an item exists in tuple:
item = 'Spinach'
print("'{}' {} exists in food_stuff tuple.".format(item, 'does' if item in food_stuff_tp else 'does not'))

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
# ================================================================================================================
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia is {}a Nordic country.".format('' if 'Estonia' in nordic_countries else 'Not '))

# Check if 'Iceland' is a nordic country
# ================================================================================================================
print("Iceland is {}a Nordic country.".format('' if 'Iceland' in nordic_countries else 'Not '))