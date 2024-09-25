#the program is about finding area, perimeter and detecting the nature of triangle
#here i am importing math module to use square root function to use it while calculating the area of triangle

import math


#here i take input of three sides of triangle
length_a=int(input("Enter the length of side a: "))
length_b=int(input("Enter the length of side b: "))
length_c=int(input("Enter the length of side c: "))


#here i calculate the perimeter,area,semiperimeter of the triangle
perimeter=length_a+length_b+length_c
s=perimeter/2
area=math.sqrt(s*(s-length_a)*(s-length_b)*(s-length_c))
#here i have printed the result
print(f"Area of a triangle is {area}m^2")
print(f"Perimeter of a triangle is {perimeter}")
#here i use the conditional statement to detect the triangle nature
if (length_a^2+length_b^2==length_c^2):
    print("it is right angle triangle")
elif  length_a^2+length_b^2>length_c^2:
    print("it is acute triangle")
else:
    print("it is obtuse triangle")
