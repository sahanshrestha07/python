#python calculator program

operator = input("Enter an operator (+ - * /): ")

num_1=int(input("Enter a number :"))
num_2=int(input("Enter another number :"))
if operator == "+":
    print(num_1+num_2)
elif operator == "-":
    print(num_1-num_2)
elif operator == "*":
    print(num_1*num_2)
elif operator == "/":
    print(num_1/num_2)
else :
    print("Invalid operator")


