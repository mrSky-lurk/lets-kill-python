# ================================================================================================================
# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# ================================================================================================================
print("Thirty" + " " + "Days" + " " + "Of" + " " + "Python")

# ================================================================================================================
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# ================================================================================================================
# Same as above


# ================================================================================================================
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# ================================================================================================================
coding_for_all = "Coding For All"

# 4. Print the variable company using _print()_.
# ================================================================================================================
print(coding_for_all)

# 5. Print the length of the company string using _len()_ method and _print()_.
print(len(coding_for_all))

# 6. Change all the characters to uppercase letters using _upper()_ method.
# ================================================================================================================
print(coding_for_all.upper())

# 7. Change all the characters to lowercase letters using _lower()_ method.
# ================================================================================================================
print(coding_for_all.lower())

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# ================================================================================================================
result = coding_for_all.capitalize()
print("Capitalize:: ", result)
result = result.title()
print("title:: ", result)
print("swapcase:: ", result.swapcase())

# 9. Cut(slice) out the first word of _Coding For All_ string.
# ================================================================================================================
print(coding_for_all.strip("Coding "))

# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
# ================================================================================================================
print("Check contains 'all' at index:: ", coding_for_all.lower().index("all"))
print("Check contains string 'odin' at all ", "odin" in coding_for_all.lower())
print("Check contains string 'folding' at all ", "folding" in coding_for_all.lower())
print("Check contains 'odin' at index:: ", coding_for_all.lower().find("odin"))
print("Count letter 'o' :: ", coding_for_all.lower().count('o'))
print("index of first 'o':: {} \t & last 'o':: {}".format(coding_for_all.lower().index('o'),
                                                          coding_for_all.lower().rindex('o')))

# 11. Replace the word coding in the string 'Coding For All' to Python.
# ================================================================================================================
print("Replaced 'Coding' to 'Folding':: ", coding_for_all.lower().replace("coding", "Folding"))

# 12. Change Python for Everyone to Python for All using the replace method or other methods.
print("Replaced 'Coding' to 'Python':: ",
      coding_for_all.lower().replace("coding", "Python").rstrip("all") + "Everyone!")

# 13. Split the string 'Coding For All' using space as the separator (split()) .
# ================================================================================================================
print(coding_for_all.split(" "))

# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# ================================================================================================================
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("Company:: ", company)
print("spliting:: ", company.split(","))
print("Joing with '#' :: ", " # ".join(company.split(",")))

# 15. What is the character at index 0 in the string _Coding For All_.
# ================================================================================================================
print(coding_for_all[0])

# 16. What is the last index of the string _Coding For All_.
# ================================================================================================================
print(coding_for_all[-1])

# 17. What character is at index 10 in "Coding For All" string.
# ================================================================================================================
print(coding_for_all[10])

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_for_everyone = "Python for everyone"


def get_acronym(value):
    new_value = ""
    for c in value.split(" "):
        new_value = new_value + c.split(" ")[0][0].upper()
    return new_value


print(get_acronym(python_for_everyone))

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# ================================================================================================================
print(get_acronym("Coding For All"))

# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# ================================================================================================================
print(coding_for_all.upper().index('C'))

# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# ================================================================================================================
print(coding_for_all.upper().index('F'))

# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# ================================================================================================================
print(coding_for_all.upper().rfind('L'))

# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# ================================================================================================================================================================================================================================
sentence_with_because = "You cannot end a sentence with because because because is a conjunction"
print("Index of the first 'Because':: ", sentence_with_because.upper().index('BECAUSE'))

# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# ================================================================================================================================================================================================================================
print("Index of the last 'Because':: ", sentence_with_because.upper().rindex("BECAUSE"))

# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# ================================================================================================================
print("Slicing it without 'because because because':: ",
      sentence_with_because.replace("because because because is ", ""))

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# ================================================================================================================
print("Position of the first occurrence of 'Because' as a word in the sentence:: ",
      sentence_with_because.upper().split(" ").index('BECAUSE'))

# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# ================================================================================================================
print("Position of the first occurrence of 'Because' as a word in the sentence:: ",
      sentence_with_because.upper().split(" ").index('BECAUSE'))

# 28. Does '\'Coding For All' start with a substring _Coding_?
# ================================================================================================================
print(coding_for_all.startswith("Coding"))

# 29. Does 'Coding For All' end with a substring _coding_?
# ================================================================================================================
print(coding_for_all.lower().endswith("coding"))

# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# ================================================================================================================
print("   {}   ".format(coding_for_all))
print("   {}   ".format(coding_for_all).strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
# ================================================================================================================
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# ================================================================================================================================================================================================================================
py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("List to string. with # delimiter:: ", "# ".join(py_lib))

# 33. Use the new line escape sequence to separate the following sentences.
#     I am enjoying this challenge.
#     I just wonder what is next.
# ================================================================================================================
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
# ================================================================================================================
print("Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35. Use the string formatting method to display the following:
# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ```
# ================================================================================================================
radius = 10
area = 3.14 * radius ** 2
print("The area of a circle with radius {} is {:.2f} meters square.".format(radius, area))

# 36. Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ================================================================================================================
num_1 = 8
num_2 = 6
print("Add:: {}".format(num_1 + num_2))
print("Subtract:: {}".format(num_1 - num_2))
print("multiply:: {}".format(num_1 * num_2))
print("divide:: {:2.2f}".format(num_1 / num_2))
print("modulus:: {}".format(num_1 % num_2))
print("floor:: {}".format(num_1 // num_2))
print("exp:: {}".format(num_1 ** num_2))