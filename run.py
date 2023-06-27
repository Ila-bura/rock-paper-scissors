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
gameOptions = ["rock", "paper", "scissors"]

"""
Function to kick off the game. Check if the option typed is valid.
Show option to abandon the game.
"""

while True:
    userTurn = input("\nChoose Rock, Paper or Scissors or Q to quit: ").lower()
    if userTurn == "q":
        break
    if userTurn not in gameOptions:
        print("Invalid input: you can only choose Rock, Paper or Scissors.")
        print("Please, try again!")
        continue

    random_number = random.randint(0, 2)
    # index number: rock 0, paper 1, scissors 2
    computerTurn = gameOptions[random_number]
    print("You chose", userTurn.capitalize() + ".")
    print("Computer chose", computerTurn.capitalize() + ".")

    if userTurn == "rock" and computerTurn == "scissors":
        print("Yay, you won!")
        userScore += 1

    elif userTurn == "paper" and computerTurn == "rock":
        print("Yay, you won!")
        userScore += 1

    elif userTurn == "scissors" and computerTurn == "paper":
        print("Yay, you won!")
        userScore += 1

    elif userTurn == "scissors" and computerTurn == "rock":
        print("Sorry, you lost!")
        computerScore += 1

    elif userTurn == "paper" and computerTurn == "scissors":
        print("Sorry, you lost!")
        computerScore += 1

    elif userTurn == "rock" and computerTurn == "paper":
        print("Sorry, you lost!")
        computerScore += 1

    elif userTurn == computerTurn:
        print("It's a tie, play once again!")
        tiedScore += 1

print("Game over! Thanks for playing")
print("You scored: ", userScore, "Computer: ", computerScore)
print("Ties: ", tiedScore)
print("Click on RUN PROGRAM to play again")
