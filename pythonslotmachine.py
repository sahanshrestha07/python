'''
program: python slot machine
author: sahan shrestha
'''
import random


def spin_row():
    symbols=['🍒','🍉','🍋','🔔','🫄']
    result = [random.choice(symbols) for i in range(3)]
    return result

def print_row(row):
    print("************")
    result = '|'.join(row)
    print(result)
    print("************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 4
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 2
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🫄':
            return bet * 10
    return 0


def main():

    balance = 100
    print("Your current balance is: $", balance)
    print("********************")
    print("Welcome to SlotMachine")
    print("Symbols: 🍒 🍉 🍋 🔔 🫄🏿")
    print("********************")

    while balance > 0:
        bet = input("place your bet amount : $")

        if not bet.isdigit():
            print("Please enter a valid bet amount")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue
        row = spin_row()
        print_row(row)
        payout = get_payout(row,bet)
        balance = balance - bet
        if payout > 0 :
            balance += payout
            print(f"You Win :{payout}")
        else:
            print(f"You Lost this round ")
        print("Current balance is " + str(balance))

        if balance < 5:
            print(f"Your Balance is {balance}")
            replay=input("Do you want to add money(y/n): ")
            if replay.upper() == 'Y':
                amount=int(input("Enter the amount you want to add: $"))
                balance = balance + amount
                print(f"Your new balance is : ${balance}")
                continue
            elif replay.upper() == 'N':
                print("You do not have much plays left")
                continue










if __name__ == '__main__':
    main()
