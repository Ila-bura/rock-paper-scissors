import random

gameOptions = ["rock", "paper", "scissors"]


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
function to display the rules
Check for valid input and prompt the user to enter the two acceptable options.
"""


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


display_rules()


"""
Function to kick off the game. Check if the option typed is valid.
Show option to abandon the game.
"""


def userTurn():
    while True:
        userTurn = input("\nPick Rock, Paper, Scissors or Q to quit: ").lower()
        if userTurn == "q":
            break
        if userTurn not in gameOptions:
            print("Invalid input! Pick one of the options or type Q to quit.")
            print("Please, check your spelling and try again!")


def get_bot_selection():
    random_number = random.randint(0, 2)
    # index number: rock 0, paper 1, scissors 2
    bot_choice = gameOptions[random_number]
    return bot_choice


def show_results(userTurn, bot_choice):
    if userTurn == bot_choice:
        print("It's a tie! Play again.")
    elif (userTurn == "rock" and bot_choice == "scissors"):
        print("You win!")
    elif (userTurn == "paper" and bot_choice == "rock"):
        print("You win!")
    elif (userTurn == "scissors" and bot_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")


def let_us_play():
    user_score = 0
    bot_score = 0
    tie_score = 0

    while True:
        if userTurn == "q":
            print("Game over! Thanks for playing!")
            break

        bot_choice = get_bot_selection()
        print("Bot chose:", bot_choice)

        if userTurn == bot_choice:
            tie_score += 1
        elif (userTurn == "rock" and bot_choice == "scissors"):
            user_score += 1
        elif (userTurn == "paper" and bot_choice == "rock"):
            user_score += 1
        elif (userTurn == "scissors" and bot_choice == "paper"):
            user_score += 1
        else:
            bot_score += 1
               
        if user_score == 3 or bot_score == 3:
            print("Game over!")
            break

            print("You scored:", user_score)
            print("Bot scored:", bot_score)
            print("Ties:", tie_score)

userTurn()