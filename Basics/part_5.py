# class car:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# car1 = car("BMW", "X5")
# print(car1.brand)
# print(car1.model)


class College:
    colleges = "abc College"

    def __init__(self, name):
        self.name = name
    def info(self):
        print(f"The name of student is {self.name} and the college is {College.colleges}")

s1 = College("Manish")
s2 = College("adi")
info1 = College("Aditya")
info1.info()

print(s1.name)
print(s2.name)
print(College.colleges)


class bankaccount:
    def __init__(self, balance,):
        self.balance = balance

    def deposit(self, amount):
        self.balance+= amount

    def show(self):
        print(f"New balance after depositing more money: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance: 
            print("Not enough balance")
        else:
            self.balance-=amount
            print(f"Amount Withdrawed: {amount}. Your remaining balance is: {self.balance}")

acc1 = bankaccount(1000)
print(f"Initial deposit: {acc1.balance}")
acc1.deposit(500)
acc1.show()
acc1.withdraw(1200)

