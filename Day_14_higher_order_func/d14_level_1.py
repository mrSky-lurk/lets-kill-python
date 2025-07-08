countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Exercises: Level 1

# Explain the difference between map, filter, and reduce.
# ================================================================================================================
print("map:: Returns iterables after applying the param=function on each one of the item\n"
      "filter:: Returns filtered list of iterables after applying the filter defined in the param=function\n"
      "reduce:: Returns one single value after performing the actions defined on param=function")

# Explain the difference between higher order function, closure and decorator
# ================================================================================================================
print("higher order function(HOF):: Can expect functions as parameter(s)....Can Return function....Can modify some feature of existing function without touching it\n"
      "closure:: Is also an HOF...Is a nested function(outer-inner)...Returns inner function which uses actual function and apply some modification...Can act as mini class where some values can be instantiated outside the function\n"
      "decorators:: Is also a closer...Mostly used as design mechanism...needs to be called as annotation(@my_decor) just before a method definition..Each time the method called the decorator will decorate/update the method")
# ================================================================================================================

# Define a call function before map, filter or reduce, see examples.
# ===============================================================================================================
# Use for loop to print each country in the countries list.
# ================================================================================================================
# Use for to print each name in the names list.
# ================================================================================================================
# Use for to print each number in the numbers list.
# ================================================================================================================