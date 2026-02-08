import sys
import random


def guess_number(name="playerOne"):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        player_choice = input(
            f"\n{name},guess witch number I am thinking of ....1, 2 or 3.\n\n"
        )

        if player_choice not in ["1", "2", "3"]:
            print("Invalid input, please choose 1, 2 or 3.")
            return play_guess_number()

        computer_choice = random.choice("123")
        print(f"\n{name}, you chose{player_choice}.")
        print(f"I was thinking about the number {computer_choice}.\n")

        player = int(player_choice)
        computer = int(computer_choice)

        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal name

            if player == computer:
                player_wins += 1
                return f"Congratulations {name}, you win!"
            else:
                return f"Sorry {name}, you lose. Better luck next time!"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\n Your win percentage: {player_wins / game_count:.2%}")
        print(f"\nDo you want to play again {name} ? (yes/no)")

        while True:
            play_again = input("\n Y for yes, N for no.\n").lower()
            if play_again not in ["y", "n"]:
                continue
            else:
                break
        if play_again == "y":
            return play_guess_number()
        else:
            print(f"\nThanks for playing, {name}! See you next time.")
            if __name__ == "__main__":
                sys.exit(f"bye {name}!")
            else:
                return

    return play_guess_number()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Play the Guess the Number Game.")

    parser.add_argument(
        "-n", "--name", metavar="name", required=True, help="Your name to play the game"
    )
    args = parser.parse_args()
    guess_my_number = guess_number(args.name)
    guess_my_number()
