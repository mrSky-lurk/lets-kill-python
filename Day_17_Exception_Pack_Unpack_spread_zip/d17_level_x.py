names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable nordic_countries,
# store Estonia and Russia in es, and ru respectively.
# ================================================================================================================
# nordic_countries = names[:5]
# print(nordic_countries)

# unpacking
*nordic_countries, es, ru = names
print(nordic_countries)
print(nordic_countries, es, ru)