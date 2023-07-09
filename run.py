"""
Import section
"""
import random
import sys

# constant with a list of acceptable options for the game
game_options = ["rock", "paper", "scissors"]


# variables for scores
user_score = 0
bot_score = 0
tie_score = 0


def get_user_selection():
    """
    Function to get user choice and check if the option typed is valid.
    If it's not, raise an error.
    """
    while True:
        try:
            user_turn = input("\nPick Rock/Paper/Scissors: ").lower()
            if user_turn not in game_options:
                raise ValueError()
        except ValueError:
            print("\nInvalid input!")
            print("You can only choose Rock, Paper, or Scissors.")
            print("Please check your spelling and try again!")
        else:
            return user_turn


def get_bot_selection():
    """
    Function to register the random computer's choice
    """
    random_number = random.randint(0, 2)
    bot_choice = game_options[random_number]
    return bot_choice


def decide_winner(user_turn, bot_choice):
    """
    Function to establish the winner or if it's a tie
    """
    if user_turn == bot_choice:
        return "tie"
    elif (user_turn == "rock" and bot_choice == "scissors") or \
            (user_turn == "paper" and bot_choice == "rock") or \
            (user_turn == "scissors" and bot_choice == "paper"):
        return "user"
    else:
        return "bot"


def update_scores(result):
    """
    Function to update the scores
    """
    global user_score, bot_score, tie_score
    if result == "tie":
        tie_score += 1
    elif result == "user":
        user_score += 1
    else:
        bot_score += 1


def display_result(result):
    """
    Function to display the results for each round
    """
    if result == "tie":
        print("\nIt's a tie, play again!")
    elif result == "user":
        print("\nYou win!")
    else:
        print("\nYou lose!")


def round_over():
    """
    Function to check if the round is over
    """
    return user_score == 3 or bot_score == 3


def display_game_result():
    """
    Function to display the final results of the game
    """
    print("-------------------------------------------")
    print("\nGame over!")
    print("\nYou scored:", user_score)
    print("Bot scored:", bot_score)
    print("Ties:", tie_score)
    if user_score > bot_score:
        print("\nYou won the game!")
    else:
        print("\nBot won the game!")
        print("Sorry, losing sucks")


def ask_restart_quit():
    """
    Function to ask the user if they want to restart or quit the game.
    """
    while True:
        choice = input("\nDo you want to play again? (Y)es/(Q)uit: ").lower()
        if choice == "y":
            reset_scores()
            print("\nHere you go, best of luck!")
            let_us_play()
            break
        elif choice == "q":
            print("\nToodaloo & thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter Y or Q.")


def let_us_play():
    """
    Function to kick off the game.
    """
    while True:
        user_turn = get_user_selection()
        bot_choice = get_bot_selection()
        print("\n You chose:", user_turn)
        print("\n Bot chose:", bot_choice)

        result = decide_winner(user_turn, bot_choice)
        update_scores(result)

        display_result(result)

        if round_over():
            display_game_result()
            ask_restart_quit()
            break


def reset_scores():
    """
    Function to reset the scores.
    """
    global user_score, bot_score, tie_score
    user_score = 0
    bot_score = 0
    tie_score = 0


def ask_rules_refresh():
    """
    Function to ask if the user needs a refresher of the rules
    """
    rules_recap = input("\n Do you need to refresh the rules? Y/N:\n").lower()
    if rules_recap == "y":
        display_rules()
    elif rules_recap == "n":
        let_us_play()
    else:
        print("Invalid input. Please enter Y or N.")
        ask_rules_refresh()


def display_rules():
    """
    Function to display the rules
    """
    print("\n - Rock smashes Scissors")
    print("\n - Scissors cut Paper")
    print("\n - Paper covers Rock")
    print("\n - Every turn you win, you score 1 point")
    print("\n - If it's a tie, no points assigned")
    print("\n - To win the game you need a total of 3 points")
    print("-------------------------------------------")
    return None


def main():
    """
    Main function to call all game functions.
    """
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
