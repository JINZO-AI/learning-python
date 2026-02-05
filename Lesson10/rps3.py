import sys
import random
from enum import Enum


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

    if player == 1 and computer == 3:
        print("🎉 you win! ")
    elif player == 2 and computer == 1:
        print("🎉 you win! ")
    elif player == 3 and computer == 2:
        print("🎉 you win! ")
    elif player == computer:
        print("😲Tie game! ")
    else:
        print("🐍 python wins! ")

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
