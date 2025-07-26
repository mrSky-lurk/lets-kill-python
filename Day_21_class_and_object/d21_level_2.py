# Exercises: Level 2
# Create a class called PersonAccount.
# It has firstname, lastname, incomes, expenses properties and
# it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods.
# Incomes is a set of incomes and its description. The same goes for expenses.
# ================================================================================================================

from person_account import PersonAccount

person = PersonAccount("Abhisek", "Chowdhury")
person.add_income("160000.00", "Salary")
person.add_income("160.60", "Divident")
person.add_expense("8000.00", "Grocery")
person.add_expense("500.00", "ATM")
person.add_income("218.67", "Cashback")

person.account_info()