# Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
# ================================================================================================================
print("Length of the list:: ", len(age))
print("Converting list to set")
age_set = set(age)
print("Length of the set:: ", len(age_set))
print("Length of the Set is {} than length of List.".format('Smaller' if len(age) > len(age_set) else 'Bigger'))

# Explain the difference between the following data types: string, list, tuple and set
# ================================================================================================================
# String - mutable, ordered, exists duplicate, Only character or string datatypes, can be sliced, elements can be modified;
# List - mutable, ordered, exists duplicate, supports multiple datatypes, elements can be modified, can be sliced, String is like a List of Characters;
# Tuple - immutable, ordered, exists duplicate, elements Un-changeable, elements can NOT be modified, can NOT be sliced;
# Set - immutable, unordered, No Duplicate, elements Un-changeable, elements can NOT be accessed, modified;



# I am a teacher and I love to inspire and teach people.
# How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.
# ================================================================================================================
sentence = "I am a teacher and I love to inspire and teach people."
to_set = set(sentence.split(" "))
print("Given sentence:: ", sentence)
print("Unique words:: ", to_set)
print("Unique characters:: ", set(sentence))
