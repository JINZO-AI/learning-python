import sys
import random
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS["ROCK"])
    # print(RPS.ROCK.value)
    # sys.exit()

    print("")
    playerchoice = input(
        "Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors :\n\n"
    )
    if playerchoice not in ["1", "2", "3"]:
        print("you must enter 1,2,3")
        return play_rps()

    player = int(playerchoice)

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("")
    print("you chose: " + str(RPS(player)).replace("RPS.", "") + ".")
    print("python chose: " + str(RPS(computer)).replace("RPS.", "") + ".")
    print("")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "🎉 you win! "
        elif player == 2 and computer == 1:
            return "🎉 you win! "
        elif player == 3 and computer == 2:
            return "🎉 you win! "
        elif player == computer:
            return "😲Tie game! "
        else:
            return "🐍 python wins! "

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count  # this tells Python that we want to use the global variable game_count instead of creating a new local variable
    game_count += 1  # this will change the value of the global variable game_count
    print("\n game count: " + str(game_count))
    print("\nPlay again?")

    while True:
        play_again = input("\nY for Yes or \nQ to Quit\n")
        if play_again.lower() not in ["y", "q"]:
            continue
        else:
            break
    if play_again.lower() == "y":
        return play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
