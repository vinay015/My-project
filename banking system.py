# parents class
class user:
    def __init__(self, name, gender, age, branch_addresss):
        self.name = name
        self.gender = gender
        self.age = age
        self.branch_adress = branch_addresss

    def show_details(self):
        print("Personal Details :")
        print("Name :-  ", self.name)
        print("Gender :-", self.gender)
        print("Age :-", self.age)
        print("Branch address\t", self.branch_address)


# child class
class bank(user):
    def __init__(self, name, gender, age, branch_address):
        super().__init__(name, gender, age, branch_address)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Amount updated is rupee is ₹:", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance is rupee ₹:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Balance updated is rupee: ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account remaining balance is rupee ₹:", self.balance)


user_name = bank("Modi", "Male", 70, "Gujarat")
user_name.show_details()
user_name.deposit(2000)
user_name.withdraw(1000)
user_name.view_balance()
