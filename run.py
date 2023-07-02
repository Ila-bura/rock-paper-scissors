import random
# constant with a list of acceptable options for the game
gameOptions = ["rock", "paper", "scissors"]

"""
Initial print statements to greet the user,
provide fun facts and introduce the game
"""

print("\nWelcome to the game of Rock Paper Scissors!")
print("-------------------------------------------")
print("\nTwo fun facts:")
print("\n1. It first appeared in China in the 17th century.")
print("\n2. Statistically, people tend to choose Scissors in the first round")
print("\n   and Rock in the second.")
print("\nNow, let's play!")
print("-------------------------------------------")

"""
Function to display the rules
Check for valid input and prompt the user to enter the two acceptable options.
"""


def display_rules():
    rulesRecap = input("Do you need a refresher of the rules? Y/N:\n").lower()
    if rulesRecap == "y":
        print("\n- Rock smashes Scissors, Scissors cut Paper")
        print("\n- Paper covers Rock")
        print("\n- Every turn you win, you score 1 point")
        print("\n- To win the game you need a total of 3 points")
    elif rulesRecap == "n":
        pass
    else:
        print("\nInvalid input. Please enter Y or N.")


"""
Function to store the random choice of the computer
Index number: rock 0, paper 1, scissors 2
"""


def get_bot_selection():
    random_number = random.randint(0, 2)
    bot_choice = gameOptions[random_number]
    return bot_choice


"""
Function to display the game results at every turn

"""


def show_results(userTurn, bot_choice):
    if userTurn == bot_choice:
        print("\nIt's a tie! Play again.")
    elif (userTurn == "rock" and bot_choice == "scissors") or \
            (userTurn == "paper" and bot_choice == "rock") or \
            (userTurn == "scissors" and bot_choice == "paper"):
        print("\nYou win!")
    else:
        print("\nYou lose!")


"""
Function to kick off the game. Prompt the user to choose an option.
Check if the option typed is valid.
Show option "q" to abandon the game.
"""


def let_us_play():
    user_score = 0
    bot_score = 0
    tie_score = 0

    while True:
        userTurn = input("\nPick Rock/Paper/Scissors or Q to quit:\n").lower()

        if userTurn == "q":
            print("\nGame over! Thanks for playing!")
            break

        if userTurn not in gameOptions:
            print("\nInvalid input")
            print("\nYou can only choose Rock, Paper or Scissors")
            print("\nPlease, check your spelling and try again!")
            continue

        bot_choice = get_bot_selection()
        print("\nYou chose:", userTurn)
        print("\nBot chose:", bot_choice)

        if userTurn == bot_choice:
            tie_score += 1
            print("\nIt's a tie! Play again!")
        elif (userTurn == "rock" and bot_choice == "scissors") or \
                (userTurn == "paper" and bot_choice == "rock") or \
                (userTurn == "scissors" and bot_choice == "paper"):
            user_score += 1
            print("\nYou win!")
        else:
            bot_score += 1
            print("\nYou lose!")

        if user_score == 3 or bot_score == 3:
            print("\nGame over!")
            print("\nYou scored:", user_score)
            print("\nBot scored:", bot_score)
            print("Ties:", tie_score)
            break


def main():
    """
    Call all game functions.
    """
    display_rules()
    let_us_play()


main()
