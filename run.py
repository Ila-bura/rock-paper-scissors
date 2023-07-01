import random

 gameOptions = ["rock", "paper", "scissors"]


def userTurn():
    while True:
        choice = input("\nPick Rock, Paper, Scissors or Q to quit: ").lower()
        if choice in gameOptions or choice == "q":
            return choice
        else:
            print("Invalid input! Pick one of the options or type Q to quit.")

def get_bot_selection():
    random_number = random.randint(0, 2)
    # index number: rock 0, paper 1, scissors 2
    return gameOptions[random_number]

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

"""
While loop to ask the user if they need a refresher of the rules of the game.
Check for valid input and prompt the user to enter the two acceptable options.
"""
# function to display the rules


def display_rules():
    rulesRecap = input("Do you need a refresher of the rules? Y/N: ").lower()
    if rulesRecap == "y":
        print("- Rock smashes Scissors, Scissors cut Paper, Paper covers Rock")
        print("- Every turn you win, you score 1 point")
        print("- To win the game you need a total of 3 points")
        return
    elif rulesRecap == "n":
        # code to continue without the recap
        return
    else:
        print("Invalid input. Please enter Y or N.")


"""
Function to kick off the game. Check if the option typed is valid.
Show option to abandon the game.
"""


def get_user_selection():
    gameOptions = ["rock", "paper", "scissors"]

    userTurn = input("\nPick Rock, Paper, Scissors or Q to quit: ").lower()
    if userTurn == "q":
        return 
    if userTurn not in gameOptions:
        print("Invalid input: you can only choose Rock, Paper or Scissors.")
        print("Please, check your spelling and try again!") 

    print("You chose", userTurn.capitalize() + ".")     


def play_round(userTurn, computerTurn):
    if userTurn == computerTurn:
        print("It's a tie")
    elif userTurn == "rock":
        if computerTurn == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("You lost")
    elif userTurn == "paper":
        if computerTurn == "rock":
            print("Paper covers rock! You win!")
        else:
            print("You lost")
    elif userTurn == "scissors":
        if computerTurn == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("You lost")


def kick_off_game():
    userScore = 0
    botScore = 0
    tiedScore = 0

    
    # function to show final scores as soon as 3 points are awarded


def show_scores(userScore, botScore, tiedScore):
    if userScore == 3 or botScore == 3:
        print("-------------------------------------------")
        print("Game over!")
    if userScore > botScore:
        print("You won the game!")
        print("You scored: ", userScore, "Computer scored: ", botScore)
        print("Ties: ", tiedScore)
        print("-------------------------------------------")
        print("Thanks for playing!")
    else:
        print("Computer won the game!")
        print("You scored: ", userScore, "Computer scored: ", botScore)
        print("Ties: ", tiedScore)
        print("-------------------------------------------")
        print("Losing sucks, but thanks for playing!")
    # function to ask the user to play again and if so, reset the scores


def playAgain():
    answer = input("Do you want to give it another go? (Y/N): ")
    if answer.lower() != "n":
        userScore = 0
        botScore = 0
        tiedScore = 0
        userTurn = True
    else:
        pass


def main():
    """
    Call all program functions.
    """
    display_rules()
    get_user_selection()
    get_bot_selection()
    decide_winner()
    show_scores()
    playAgain()


main()