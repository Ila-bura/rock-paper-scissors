import random
import sys
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


# function to get user choice. check if the option typed is valid.
def get_user_selection():
    while True:
        user_turn = input("\nPick Rock/Paper/Scissors: ").lower()
        if user_turn not in game_options:
            print("\nInvalid input!")
            print("You can only choose Rock, Paper, or Scissors.")
            print("Please check your spelling and try again!")
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


# function to reset the scores
def reset_scores():
    global user_score, bot_score, tie_score
    user_score = 0
    bot_score = 0
    tie_score = 0


# function to ask the user if they want to restart or quit the game
def ask_restart_quit():
    while True:
        choice = input("\nDo you want to play again? (Y)es/(Q)uit: ").lower()
        if choice == "y":
            reset_scores()
            print("\nHere you go, best of luck!")
            let_us_play()
            break
        elif choice == "q":
            print("\nTodaloo & thanks for playing!")
            sys.exit()
        else:
            print("Invalid input. Please enter Y or Q.")


# function to kick off the game. Prompt the user to choose an option.
def let_us_play():
    while True:
        user_turn = get_user_selection()
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
            else:
                print("\n Bot won the game!")
                print("\n Sorry, losing sucks")
            ask_restart_quit()
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
