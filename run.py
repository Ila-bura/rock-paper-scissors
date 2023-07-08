import random
# constant with a list of acceptable options for the game
game_options = ["rock", "paper", "scissors"]


# variables for scores
user_score = 0
bot_score = 0
tie_score = 0


# function to ask if the user needs a refresher of the rules
def ask_rules_refresh():
    rules_recap = input("\n Do you need to refresh the rules? Y/N:\n").lower()
    if rules_recap == "y":
        display_rules()
    elif rules_recap == "n":
        let_us_play()
    else:
        print("Invalid input. Please enter Y or N.")
        ask_rules_refresh()


# function to display the rules
def display_rules():
    print("\n - Rock smashes Scissors")
    print("\n - Scissors cut Paper")
    print("\n - Paper covers Rock")
    print("\n - Every turn you win, you score 1 point")
    print("\n - To win the game you need a total of 3 points")
    print("-------------------------------------------")
    return None


# function to get user choice
def get_user_selection():
    user_turn = input("\n Pick Rock/Paper/Scissors or Q to quit:\n").lower()
    if user_turn == "q":
        print("\n Game over! Thanks for playing!")
        return None
    elif user_turn not in game_options:
        print("\n Invalid input!")
        print("\n You can only choose Rock, Paper, or Scissors.")
        print("\n Please check your spelling and try again!")
        return get_user_selection()
    else:
        return user_turn


# function to get computer choice
def get_bot_selection():
    random_number = random.randint(0, 2)
    bot_choice = game_options[random_number]
    return bot_choice


# function to establish the winner
def decide_winner(user_turn, bot_choice):
    if user_turn == bot_choice:
        return "tie"
    elif (user_turn == "rock" and bot_choice == "scissors") or \
            (user_turn == "paper" and bot_choice == "rock") or \
            (user_turn == "scissors" and bot_choice == "paper"):
        return "user"
    else:
        return "bot"


# function to update the scores
def update_scores(result):
    global user_score, bot_score, tie_score
    if result == "tie":
        tie_score += 1
    elif result == "user":
        user_score += 1
    else:
        bot_score += 1


"""
Function to kick off the game. Prompt the user to choose an option.
Check if the option typed is valid.
"""


def let_us_play():
    while True:
        user_turn = get_user_selection()
        if user_turn is None:
            break

        bot_choice = get_bot_selection()
        print("\n You chose:", user_turn)
        print("\n Bot chose:", bot_choice)

        result = decide_winner(user_turn, bot_choice)
        update_scores(result)

        if result == "tie":
            print("\n It's a tie, play again!")
        elif result == "user":
            print("\n You win!")
        else:
            print("\n You lose!")

        if user_score == 3 or bot_score == 3:
            print("-------------------------------------------")
            print("\n Game over!")
            print("\n You scored:", user_score)
            print("\n Bot scored:", bot_score)
            print("\n Ties:", tie_score)
            if user_score > bot_score:
                print("\n You won the game!")
                print("\n Thanks for playing!")
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

    ask_rules_refresh()

    let_us_play()


main()
