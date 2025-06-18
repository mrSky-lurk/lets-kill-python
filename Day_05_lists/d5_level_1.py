# Declare an empty list
# ================================================================================================================
empty_list = []

# Declare a list with more than 5 items
# ================================================================================================================
six_items = ['Stone', 'Barrel', 69, 'Hogs', 'Swords', 'King']
print("Items:: ", six_items)

# Find the length of your list
# ================================================================================================================
print("length:: ", len(six_items))

# Get the first item, the middle item and the last item of the list
# ================================================================================================================
print("First item:: ", six_items[0])
print("Last item:: ", six_items[-1])
print("Middle item:: ", six_items[int(len(six_items) / 2)])

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
# ================================================================================================================
mixed_data_types = ['Billu', 30, '5\'2"', 'Married', 'Kolkata']
print(mixed_data_types)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
# ================================================================================================================
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
# ================================================================================================================
print("IT companies:: ", it_companies)

# Print the number of companies in the list
# ================================================================================================================
print("Number of Companies:: ", len(it_companies))

# Print the first, middle and last company
# ================================================================================================================
print("First Company:: ", it_companies[0])
print("Last Company:: ", it_companies[-1])
print("Middle Company:: ", it_companies[int(len(it_companies) / 2)])

# Print the list after modifying one of the companies
# ================================================================================================================
it_companies[2] = 'Netflix'
print("Modified 3rd Company:: ", it_companies)

# Add an IT company to it_companies
# ================================================================================================================
it_companies.append('Microsoft')
print("Added new Company at the end", it_companies)

# Insert an IT company in the middle of the companies list
# ================================================================================================================
it_companies.insert(3, 'X')
print("Inserted new Company at 4th place", it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
# ================================================================================================================
get_index = it_companies.index('Netflix')
it_companies[get_index] = it_companies[get_index].upper()
print("Modified IT companies:: ", it_companies)

# Join the it_companies with a string '#;  '
# ================================================================================================================
print("Joining with a '#':: ", " #; ".join(it_companies))

# Check if a certain company exists in the it_companies list.
# ================================================================================================================
print("Check if Facebook exists:: ", 'Facebook' in it_companies)
print("Check if Flipkart exists:: ", 'Flipkart' in it_companies)

# Sort the list using sort() method
# ================================================================================================================
it_companies.sort()
print("Sorted list:: ", it_companies)

# Reverse the list in descending order using reverse() method
# ================================================================================================================
it_companies.sort(reverse=True)
print("Reverse sorted list: ", it_companies)

# Slice out the first 3 companies from the list
# ================================================================================================================
print("First 3 companies:: ", it_companies[0:3])

# Slice out the last 3 companies from the list
print("Last 3 companies:: ", it_companies[-3:])

# Slice out the middle IT company or companies from the list
# ================================================================================================================
# it_companies.append("LOCO")
print(it_companies)
if (len(it_companies) % 2 == 0):
    print("Mid Companies:: ", it_companies[int(len(it_companies) / 2) - 1:int(len(it_companies) / 2) + 1])
else:
    print("Mid Companies:: ", it_companies[int(len(it_companies) / 2)])

# Remove the first IT company from the list
# ================================================================================================================
it_companies.pop(0)
print("Removed first company:: ", it_companies)

# Remove the middle IT company or companies from the list
# ==========================================================================================================================
print("Initial list:: ", it_companies)
popped_index = int(len(it_companies) / 2)
if (len(it_companies) % 2 != 0):
    print("Removing:: ", it_companies.pop(int(len(it_companies) / 2)))
else:
    print("Removing:: ", it_companies.pop(int(len(it_companies) / 2)))
    print("Removing:: ", it_companies.pop(int(len(it_companies) / 2)))
print("List after removal of companies:: ", it_companies)

# Remove the last IT company from the list
# ================================================================================================================
print("List after removal of last company i.e. '{}':: {}".format(it_companies.pop(-1), it_companies))

# Remove all IT companies from the list
# ================================================================================================================
it_companies.clear()
print("Cleared list:: ", it_companies)
# Destroy the IT companies list
del it_companies
print("List ref Destroyed")

# Join the following lists:
# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question . Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
# ======================================================================================================================================
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined_list = front_end + back_end
print("Joined list:: ", joined_list)
full_stack = joined_list.copy()
print("Copied joined list to full_stack:: ", full_stack)
index_of_redux = full_stack.index('Redux')
full_stack.insert(index_of_redux + 1, 'Python')
full_stack.insert(index_of_redux + 2, 'SQL')
print(full_stack)
