# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Exercises: Level 1
# Find the length of the set it_companies
# ================================================================================================================
print(len(it_companies))

# Add 'Twitter' to it_companies
# ================================================================================================================
it_companies.add('Twitter')
print("Added Twitter:: ", it_companies)

# Insert multiple IT companies at once to the set it_companies
# ================================================================================================================
it_companies.update(['Intel', 'Firefox', 'TCS', 'Apple', 'Microsoft'])
print("Updated new IT companies:: ", it_companies)

# Remove one of the companies from the set it_companies
# ================================================================================================================
it_companies.remove('TCS')
# it_companies.remove('IAmNotHere')
print("Removed TCS:: ", it_companies)

# What is the difference between remove and discard
# ================================================================================================================
it_companies.discard('Apple')
it_companies.discard('IAmNotHere')
print("Discarded Apple:: ", it_companies)


