import random

"""
Initial print statements to greet the user and introduce the game
"""

print("Welcome to the game of Rock Paper Scissors!")
print("-------------------------------------------")
print("Two fun facts:")
print("1. It first appeared in China in the 17th century.")
print("2. Statistically, people tend to choose Scissors in the first round")
print("and Rock in the second.")
print("Now, let's play!")
print("-------------------------------------------")


"""
Create game variables to store the scores.
"""

userScore = 0
botScore = 0
tiedScore = 0
gameOptions = ["rock", "paper", "scissors"]

"""
While loop to ask the user if they need a refresher of the rules of the game.
Check for valid input and prompt the user to enter the two acceptable options.
"""

while True:
    rulesRecap = input("Do you need a refresher of the rules? Y/N: ").lower()
    if rulesRecap == "y":
        print("- Rock smashes Scissors, Scissors cut Paper, Paper covers Rock")
        print("- Every turn you win, you score 1 point")
        print("- To win the game you need a total of 3 points")
        break
    elif rulesRecap == "n":
        # code to continue without the recap
        break
    else:
        print("Invalid input. Please enter Y or N.")

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
        print("Please, check your spelling and try again!")
        continue

    random_number = random.randint(0, 2)
    # index number: rock 0, paper 1, scissors 2
    computerTurn = gameOptions[random_number]
    print("You chose", userTurn.capitalize() + ".")
    print("Computer chose", computerTurn.capitalize() + ".")

    if userTurn == "rock" and computerTurn == "scissors":
        print("Rock smashes scissors! You win!")
        userScore += 1

    elif userTurn == "paper" and computerTurn == "rock":
        print("Paper covers rock! You win!")
        userScore += 1

    elif userTurn == "scissors" and computerTurn == "paper":
        print("Scissors cuts paper! You win!")
        userScore += 1

    elif userTurn == "scissors" and computerTurn == "rock":
        print("Rock smashes scissors! You lose!")
        botScore += 1

    elif userTurn == "paper" and computerTurn == "scissors":
        print("Scissors cuts paper. You lose!")
        botScore += 1

    elif userTurn == "rock" and computerTurn == "paper":
        print("Paper covers rock! You lose!")
        botScore += 1

    else:
        print("It's a tie! Play again")
        tiedScore += 1
    # function to show final scores as soon as 3 points are awarded
    if userScore == 3 or botScore == 3:
        print("-------------------------------------------")
        print("Game over!")
        if userScore > botScore:
            print("You won the game!")
            print("You scored: ", userScore, "Computer scored: ", botScore)
            print("Ties: ", tiedScore)
            print("-------------------------------------------")
            print("Thanks for playing!")
            print("Click on RUN PROGRAM for another round")
        else:
            print("Computer won the game!")
            print("You scored: ", userScore, "Computer scored: ", botScore)
            print("Ties: ", tiedScore)
            print("-------------------------------------------")
            print("Losing sucks, but thanks for playing!")
            print("Click RUN PROGRAM to give it another go.")
        break
