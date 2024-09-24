#Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Enter your unit kilograms or pounds (K or L): ")

if unit == "K" :
    weight = weight * 2.204
    print("Your weight is {:.2f} in pounds".format(weight))
elif unit == "L" :
    weight = weight * 0.453
    print("Your weight is {:.2f} in kilograms".format(weight))
