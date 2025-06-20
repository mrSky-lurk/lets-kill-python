# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# ================================================================================================================
has_skills = 'skills' in person.keys()
print("Person has skillset:: ", has_skills)
if has_skills:
    print("The middle skill:: ", person.get('skills')[int(len(person.get('skills')) / 2)])
else:
    print("Skills not assigned to the person.")

#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# ================================================================================================================
if has_skills and 'Python' in person.get('skills'):
    print("Person knows Python")
else:
    print("Person does not know Python")

#  * If a person skills has only JavaScript and React,
#  print('He is a front end developer'),
#  if the person skills has Node, Python, MongoDB,
#  print('He is a backend developer'),
#  if the person skills has React, Node and MongoDB,
#  Print('He is a fullstack developer'),
#  else print('unknown title')
#  - for more accurate results more conditions can be nested!
# ================================================================================================================
frontend_dev={'JavaScript', 'React'}
backend_dev={'Node', 'Python', 'MongoDB'}
user_input = set(input("Enter skills, comma separated:: ").split(","))
if user_input.issubset(frontend_dev):
    if user_input == frontend_dev:
        print("You are a hardcore front-end developer")
    else:
        print("you are on the way to become a frontend developer. Few skills to add:: ", user_input.symmetric_difference(frontend_dev))
elif user_input.issubset(backend_dev):
    if user_input == backend_dev:
        print("you are a hardcore back-end developer")
    else:
        print("You are on the way to become a backend developer. Few skills to add:: ", user_input.symmetric_difference(frontend_dev))
elif user_input.issubset(frontend_dev.union(backend_dev)):
    if user_input == frontend_dev.union(backend_dev):
        print("Hello Mr. Knows-it-all")
    else:
        print("To become full stack developer, you need {} more skill(s) : {}".format(len(user_input.symmetric_difference(frontend_dev.union(backend_dev))), user_input.symmetric_difference(frontend_dev.union(backend_dev))))
else:
    print("You are something different")


#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
# ================================================================================================================
marrital_status = input("Is marriyed? (yes/no):: ").upper()
place = input("Country of residence:: ").upper()
if marrital_status == 'NO' and place == 'Finland'.upper():
    print("Are you looking for - Asabeneh Yetayeh lives in Finland. He is married.")
else:
    print("No idea")

