questions = ("How many elements are in the periodic table?:",
             "Which animal lays the largest eggs?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest?: ")


options = (("A"),("B"),("C"),("D"))
guess = []
answers = (("A"),
           ("B"),
           ("C"),
           ("D"),
           )


for question in questions:
    print("--------------")
    print(question)
    for option in options:
        print(option)
    for guesses in answers:
        guess = input("Enter your guess")
        if guess == options[0]or guess == options[1] or guess == options[2] or guess == options[3]:
            if guess == answers[questions.index(guess)]:
                print("Correct")
            else :
                print("Incorrect")
        else:
            print("your guess is invalid")



