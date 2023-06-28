import random

"""
Initial print statements to greet the user and introduce the game
"""

print("Welcome to the game of Rock Paper Scissors!")
print("-------------------------------------------")
print("Two fun facts about this game:")
print("1. It first appeared in China in the 17th century.")
print("2. Statistically, people tend to choose Scissors in the first round")
print("and Rock in the second.")
print("Let's play!")
print("-------------------------------------------")


"""
Create game variables
Function to kick off the game. Check if the option typed is valid.
Show option to abandon the game.
"""

userScore = 0
computerScore = 0
tiedScore = 0
gameOptions = ["rock", "paper", "scissors"]

"""
Ask the user if they need a refresher of the rules of the game.
"""

while True:
    rulesRecap = input("Do you want a refresher of the rules? Y/N: ").lower()
    if rulesRecap == "y":
        print("Rock beats Scissors, Scissors beat Paper, Paper beats Rock")
        break
    elif rulesRecap == "n":
        # code to continue without refresher
        break
    else:
        print("Invalid input. Please enter Y or N.")


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

    else:
        print("It's a tie, play once again!")
        tiedScore += 1

print("Game over! Thanks for playing")
print("You scored: ", userScore, "Computer: ", computerScore)
print("Ties: ", tiedScore)
print("Click on RUN PROGRAM to play again")
