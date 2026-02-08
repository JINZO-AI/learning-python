import sys
from rps import rps
from guess_number import guess_number


def play_game(name="player_1"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\nWelcome back {name} to the Arcade menu!")

        player_choice = input(
            "\nPlease choose a game:\n1. Rock, Paper, Scissors\n2. Guess the Number\n3. Exit\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print("Invalid input, please choose 1, 2 or 3.")
            return play_game(name)

        welcome_back = True

        if player_choice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == "2":
            guess_the_number = guess_number(name)
            guess_the_number()
        else:
            print(f"\nThanks for playing, {name}! See you next time.")
            sys.exit(f"bye {name}!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Welcome to the Arcade! Choose a game to play."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    print(f"\n {args.name}")

    play_game(args.name)
