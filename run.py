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


def whoIsTheWinner(userTurn, computerTurn):
    if (userTurn == "Rock" and computerTurn == "Paper"):
        print("Sorry, you lost!")
        return "Computer"
    elif (userTurn == "Rock" and computerTurn == "Scissors"):
        print("Yay, you won!")
        return "You"
    elif (userTurn == "Scissors" and computerTurn == "Paper"):
        print("Yay, you won!")
        return "You"
    elif (userTurn == "Scissors" and computerTurn == "Rock"):
        print("Sorry, you lost!")
        return "Computer"
    elif (userTurn == "Paper" and computerTurn == "Rock"):
        print("Yay, you won!")
        return "You"
    elif (userTurn == "Paper" and computerTurn == "Scissors"):
        print("Sorry, you lost!")
        return "Computer"
    else:
        print("It's a tie, play once again!")
        return "Tie"


"""
Function to kick off the game. Validate the score
"""

while(userScore != 3 and computerScore != 3):
    while True:
        userTurn = input("\nYour turn to choose one: Rock, Paper or Scissors: ")
        if(userTurn == "Rock" or userTurn == "Paper" or userTurn == "Scissors"):
            break
        else: 
            print("You can only choose between Rock, Paper or Scissors. Try again.")

