'''
author: sahan shrestha
program: vending machine
'''


class VendingMachine:
    def __init__(self):
        self.soda = 10
        self.coffee = 10
        self. water = 10
        self.amount = 0
    def buy_operation(self):
            self.buy_input = input(":> ")
            if self.buy_input == '1':
                self.soda = self.soda - 1 if self.soda > 0 else print("we don't have soda")
            if self.buy_input == '2' :
                self.coffee = self.coffee - 1 if self.coffee > 0 else print("we don't have coffee")
            if self.buy_input == '3' :
                self.water = self.water - 1 if self.water > 0 else print("we don't have water")
    def inventory(self):
            print(f"Soda = {self.soda} bottles  ")
            print(f"Coffee = {self.coffee} bottles  ")
            print(f"Water = {self.water} bottles  ")
    def restock(self):
            print("Please select an option")
            print("1 - Soda \n2 - Coffee\n3 - Water")
            self.restock_input = input()
            if self.restock_input == '1':
                self.amount = int(input("please enter the amount you want to restock"))
                self.soda += self.amount
            if self.restock_input == '2':
                self.amount = int(input("please enter the amount you want to restock"))
                self.coffee += self.amount
            if self.restock_input == '3':
                self.amount = int(input("please enter the amount you want to restock"))
                self.water += self.amount

op = VendingMachine()
while True:
    operation = input("Please select an operation: ")
    if operation.lower() == "quit" or operation.lower() == "q":
        break
    else:
        if operation.lower() == 'buy':
            print("Please select an option")
            print("1 - Soda \n2 - Coffee\n3 - water")
            op.buy_operation()
            continue
        elif operation.lower() == 'inventory':
            op.inventory()
            continue
        elif operation.lower() == 'restock':
            op.restock()
            continue
        else :
            print("enter valid operation")
            continue







