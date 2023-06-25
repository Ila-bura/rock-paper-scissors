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
print("A robot developed in Japan wins with 100 per cent chance.")
print("It analyzes movement of your hand muscles to predict your choice.")

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
        retun "You"
    elif (user == "Scissors" and computer == "Paper"):
        print("Yay, you won!")
        retun "You"
    elif (user == "Scissors" and computer == "Rock"):
        print("Sorry, you lost!")
        return "Computer"
    elif (user == "Paper" and computer == "Rock"):
        print("Yay, you won!")
        retun "You"
    elif (user == "Paper" and computer == "Scissors"):
        print("Sorry, you lost!")
        return "Computer"
    else:
        print("It's a tie, play once again!")
        return "Tie"