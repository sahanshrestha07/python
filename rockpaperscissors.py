import random
options = ("rock","paper","scissors")
player = None
computer = random.choice(options)
player = input("Enter a choice(rock,paper,scissors):")
print(f"Player: {player}")
print(f"Computer : {computer})
all_case_result = {"rock" : "scissors","paper" : "rock", "scissors" : "paper"}
if player == all_case_result[]