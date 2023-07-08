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


# function to get user choice
def get_user_selection():
    while True:
        userTurn = input("\n Pick Rock/Paper/Scissors or Q to quit:\n").lower()
        if userTurn == "q":
            print("\n Game over! Thanks for playing!")
            return None
        if userTurn in gameOptions:
            return userTurn
        print("\n Invalid input!")
        print("\n You can only choose Rock, Paper, or Scissors.")
        print("\n Please check your spelling and try again!")


# function to get computer choice
def get_bot_selection():
    random_number = random.randint(0, 2)
    bot_choice = gameOptions[random_number]
    return bot_choice


# function to establish the winner
def decide_winner(userTurn, bot_choice):
    if userTurn == bot_choice:
        return "tie"
    elif (userTurn == "rock" and bot_choice == "scissors") or \
            (userTurn == "paper" and bot_choice == "rock") or \
            (userTurn == "scissors" and bot_choice == "paper"):
        return "user"
    else:
        return "bot"


# function to reset the scores to zero
def reset_scores():
    user_score = 0
    bot_score = 0
    tie_score = 0
    return user_score, bot_score, tie_score


"""
Function to kick off the game. Prompt the user to choose an option.
Check if the option typed is valid.
Show option "q" to abandon the game.
"""


def let_us_play():
    user_score, bot_score, tie_score = reset_scores()

    while True:
        userTurn = get_user_selection()
        if userTurn is None:
            break

        bot_choice = get_bot_selection()
        print("\n You chose:", userTurn)
        print("\n Bot chose:", bot_choice)

        result = decide_winner(userTurn, bot_choice)
        if result == "tie":
            tie_score += 1
            print("\n It's a tie, play again!")
        elif result == "user":
            user_score += 1
            print("\n You win!")
        else:
            bot_score += 1
            print("\n You lose!")

        if user_score == 3 or bot_score == 3:
            print("-------------------------------------------")
            print("\n Game over!")
            print("\n You scored:", user_score)
            print("\n Bot scored:", bot_score)
            print("\n Ties:", tie_score)
            if user_score > bot_score:
                print("\n You won the game!")
            else:
                print("\n Bot won the game!")
                print("\n Losing sucks, but thanks for playing!")

            print("-------------------------------------------")
            print("\n Click on Run Program to play again")
            break


def main():
    print("\n Welcome to the game of Rock Paper Scissors!")
    print("-------------------------------------------")
    print("\n Two fun facts:")
    print("\n 1. It first appeared in China in the 17th century.")
    print("\n 2. People tend to choose Scissors in the first round")
    print("\n    and Rock in the second.")
    print("\n Now, let's play!")
    print("-------------------------------------------")

    rulesRecap = input("\n Do you need to refresh the rules? Y/N:\n").lower()
    if rulesRecap == "y":
        display_rules()

    let_us_play()


main()
