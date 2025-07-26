class PersonAccount:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = dict()
        self.expenses = dict()
        self.acc_statement = dict()

    def add_income(self, income, desc):
        self.update_account(desc + ":" + income, 'CREDIT')
        self.incomes[desc.upper()] = float(income)

    def add_expense(self, expense, desc):
        self.update_account(desc + ":" + expense, 'DEBIT')
        self.expenses[desc.upper()] = float(expense)

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def update_account(self, desc, type):
        self.acc_statement[desc] = type

    def account_info(self):
        print("\n\n=========================================================")
        print(f"Account Holder: {self.first_name} {self.last_name}")
        print("=========================================================")
        for elm in self.acc_statement.items():
            print(elm[1] + " \t|-----|\t " + elm[0])
        print("=========================================================")
        print("Total income: ", self.total_income())
        print("Total Expense: ", self.total_expense())
        print("=========================================================")
        print("A/C Balance: ", float(self.total_income()) - float(self.total_expense()))

