import sys
import random
from enum import Enum


def rps(name="Player_1"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        print("")
        playerchoice = input(
            f"{name}, enter...\n1 for Rock : \n2 for Paper :  \n3 for Scissors :\n\n"
        )
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, you must enter 1,2,3")
            return play_rps()

        player = int(playerchoice)

        computer_choice = random.choice("123")
        computer = int(computer_choice)

        print("")
        print(f"{name}, you chose: {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"python chose: {str(RPS(computer)).replace('RPS.', '').title()}.")
        print("")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name},You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name},You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉{name}, You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\n sorry ,{name}...🥺"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\n game count: {game_count}")
        print(f"\n {name}'s wins : {player_wins}")
        print(f"\n python wins : {python_wins}")
        print(f"\nPlay again, {name}?")

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
            sys.exit(f"Bye {name}! 👋")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provide a personalized game experience."
    )
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="the name of the person playing the game.",
    )
    args = parser.parse_args()

    rock_paper_scissor = rps(args.name)
    rock_paper_scissor()
