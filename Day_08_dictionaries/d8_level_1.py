# Create an empty dictionary called dog
# ================================================================================================================
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
# ================================================================================================================
dog = {
    'name': 'Rimmo',
    'color': 'Black',
    'bread': 'Lab',
    'legs': 5,
    'age': 2
}

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
# ================================================================================================================
student = {
    'first_name': 'Bran',
    'last_name': 'Stark',
    'gender': 'male',
    'age': 14,
    'marital_status': 'unmarried',
    'skills': ['archery', 'swords', 'future sighting', 'climbing'],
    'country': 'Westeros',
    'city': 'Winterfel',
    'tag': 'Winter is coming'
}
# Get the length of the student dictionary
# ================================================================================================================
print("Length of studet dict:: ", len(student))

# Get the value of skills and check the data type, it should be a list
# ================================================================================================================
print("skillset:: ", student.get('skills'))
print("skills data type:: ", type(student.get('skills')))

# Modify the skills values by adding one or two skills
# ================================================================================================================
student.get('skills').append('warging')
print("skillset:: ", student.get('skills'))

# Get the dictionary keys as a list
# ================================================================================================================
print("student key list:: ", student.keys())

# Get the dictionary values as a list
# ================================================================================================================
print("all values:: ", student.values())

# Change the dictionary to a list of tuples using items() method
# ================================================================================================================
print("full Dict to List of tuples:: ", student.items())
student_list = list(student.items())
print(student_list[2])

# Delete one of the items in the dictionary
# ================================================================================================================
student.pop('age')
print(student)
del student['last_name']
print(student)

# Delete one of the dictionaries
del dog

