import random
# constant with a list of acceptable options for the game
gameOptions = ["rock", "paper", "scissors"]


# function to display the rules
def display_rules():
    print("\n - Rock smashes Scissors")
    print("\n - Scissors cut Paper")
    print("\n - Paper covers Rock")
    print("\n - Every turn you win, you score 1 point")
    print("\n - To win the game you need a total of 3 points")
    print("-------------------------------------------")

#function to get user choice
def get_user_selection():
    
def get_bot_selection():
    random_number = random.randint(0, 2)
    bot_choice = gameOptions[random_number]
    return bot_choice


"""
Initial print statements to greet the user,
provide fun facts and introduce the game
"""

print("\n Welcome to the game of Rock Paper Scissors!")
print("-------------------------------------------")
print("\n Two fun facts:")
print("\n 1. It first appeared in China in the 17th century.")
print("\n 2. Statistically, people tend to choose Scissors in the first round")
print("\n and Rock in the second.")
print("\n Now, let's play!")
print("-------------------------------------------")

"""
Check for valid input and prompt the user to enter the two acceptable options.
"""


def display_rules():
    rulesRecap = input("\n Do you need to refresh the rules? Y/N:\n").lower()
    if rulesRecap == "y":
        print("\n - Rock smashes Scissors")
        print("\n - Scissors cut Paper")
        print("\n - Paper covers Rock")
        print("\n - Every turn you win, you score 1 point")
        print("\n - To win the game you need a total of 3 points")
        print("-------------------------------------------")
    elif rulesRecap == "n":
        pass
    else:
        print("\n Invalid input. Please enter Y or N.")
        display_rules()


"""
Function to store the random choice of the computer
Index number: rock 0, paper 1, scissors 2
"""



"""
Function to display the game results at every turn

"""


def show_results(userTurn, bot_choice):
    if userTurn == bot_choice:
        print("\n It's a tie! Play again.")
    elif (userTurn == "rock" and bot_choice == "scissors") or \
            (userTurn == "paper" and bot_choice == "rock") or \
            (userTurn == "scissors" and bot_choice == "paper"):
        print("\n You win!")
    else:
        print("\n You lose!")


"""
Function to ask the user if they want to play another round
at the end of the first game.

"""


def play_again():
    while True:
        want_more = input("\n Want to give it another go? (Y/N): ").lower()

        if want_more == "y":
            print("\n Here you go, best of luck!")
            return True

        elif want_more == "n":
            print("\n Thanks for playing!")
            return False

        else:
            print("\n Invalid input. Please enter Y or N.")


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
        userTurn = input("\n Pick Rock/Paper/Scissors or Q to quit:\n").lower()

        if userTurn == "q":
            print("\n Game over! Thanks for playing!")
            break

        if userTurn not in gameOptions:
            print("\n Invalid input")
            print("\n You can only choose Rock, Paper or Scissors")
            print("\n Please, check your spelling and try again!")
            continue

        bot_choice = get_bot_selection()
        print("\n You chose:", userTurn)
        print("\n Bot chose:", bot_choice)

        if userTurn == bot_choice:
            tie_score += 1
            print("\n It's a tie, play again!")
        elif (userTurn == "rock" and bot_choice == "scissors") or \
                (userTurn == "paper" and bot_choice == "rock") or \
                (userTurn == "scissors" and bot_choice == "paper"):
            user_score += 1
            print("\n You win!")
        else:
            bot_score += 1
            print("\n You lose!")

        if user_score == 3 or bot_score == 3:
            print("-------------------------------------------")
            print("\n Game over!")
            if user_score > bot_score:
                print("\n You won the game!")
                print("\n You scored:", user_score)
                print("\n Bot scored:", bot_score)
                print("\n Ties:", tie_score)
            else:
                print("\n Bot won the game!")
                print("\n You scored:", user_score)
                print("\n Bot scored:", bot_score)
                print("\n Ties:", tie_score)
                print("\n Losing sucks, but thanks for playing!")
                print("-------------------------------------------")

            if not play_again():
                break


def main():
    """
    Call all game functions.
    """
    display_rules()
    let_us_play()


main()
