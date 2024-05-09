# parents class
class user:
    def __init__(self, name, gender, age, branch_adresss):
        self.name = name
        self.gender = gender
        self.age = age
        self.branch_adress = branch_adresss

    def show_details(self):
        print("personal details:")
        print("name  ", self.name)
        print("gender", self.gender)
        print("age   ", self.age)
        print("branch address\t", self.branch_adress)


# child class
class bank(user):
    def __init__(self, name, gender, age, branch_address):
        super().__init__(name, gender, age, branch_address)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("amount amount updated is rupee is :", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("insufficient balance is rupee:", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("balance updated is rupee: ", self.balance)

    def view_balance(self):
        self.show_details()
        print("account remaining balance is rupee :", self.balance)


user_name = bank("Modi", "male", 70, "Gujarat")
user_name.show_details()
user_name.deposit(2000)
user_name.withdraw(1000)
user_name.view_balance()
