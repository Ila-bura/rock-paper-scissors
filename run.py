import random

"""
Initial print statements to greet the user and introduce the game
"""

print("Welcome to the game of Rock Paper Scissors!")
print("-------------------------------------------")
print("Fun facts about this game:")
print("It first appeared in China in the 17th century.")
print("Statistically people choose Scissors in the first round")
print("and Rock in the second.")

"""
Create game variables
"""
userScore = 0
computerScore = 0
tiedScore = 0
gameOptions = ["Rock", "Paper", "Scissors"]

"""
Function to check who is the winner for each round depending on possible
combinations
"""


def whoIsTheWinner(user, computer):
    if (user == "Rock" and computer == "Paper"):
        print("Sorry, you lost!")
        return "Computer"
    elif (user == "Rock" and computer == "Scissors"):
        print("Yay, you won!")
        return "You"
    elif (user == "Scissors" and computer == "Paper"):
        print("Yay, you won!")
        return "You"
    elif (user == "Scissors" and computer == "Rock"):
        print("Sorry, you lost!")
        return "Computer"
    elif (user == "Paper" and computer == "Rock"):
        print("Yay, you won!")
        return "You"
    elif (user == "Paper" and computer == "Scissors"):
        print("Sorry, you lost!")
        return "Computer"
    else:
        print("It's a tie, play once again!")
        return "Tie"


"""
Function to kick off the game. Validate the score
"""

while (userScore != 3 and computerScore != 3):
    while True:
        user = input("\nYour turn to choose Rock, Paper or Scissors: ").lower()
        if (user == "Rock" or user == "Paper" or user == "Scissors"):
            break
        else: 
            print("You can only choose Rock, Paper or Scissors. Try again.")

"""
Generate random computer choice
"""

computer = random.choice(gameOptions)

"""
Print results
"""

print("You: ", user)
print("Computer: ", computer)
result = whoIsTheWinner(user, computer)