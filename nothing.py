#WAP to enter a set of fruits in a tuple and print the required fruit according to the users input. use function too
from past.builtins import xrange

user = str(input("Enter to check if your fruit is in the list"))
def detection_function(user):
    fruits = ('apple', 'banana', 'cherry')
for x in fruits:
    if user == fruits[x]:
        print("The you have entered is in the fruits list")
        break
    else:
        print("The fruit is not on the list")
        break


