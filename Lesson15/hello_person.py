def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


if __name__ == "__main__":
    import argparse  # argparse is a module for parsing command-line arguments

    parser = argparse.ArgumentParser(
        description="Provide a personal greeting."  # This is a description of what the program does, which will be displayed when the user runs the program with the --help flag.
    )
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",  # This line adds an argument to the parser. The first two arguments are the short and long versions of the argument, which can be used when running the program. The metavar argument specifies the name of the argument that will be displayed in the help message.
        required=True,
        help="the name of the person to greet",  # This line specifies that the argument is required and provides a help message that will be displayed when the user runs the program with the --help flag.
    )
    parser.add_argument(
        "-l",
        "--lang",
        metavar="language",
        required=True,
        choices=["English", "Spanish", "German"],
        help="the language of the greeting.",
    )
    args = parser.parse_args()  # This line parses the command-line arguments and stores them in the args variable.
    hello(
        args.name, args.lang
    )  # This line calls the hello_person function with the name and language provided by the user.

    # msg = f"hello{args.name}!"  # This line creates a greeting message using the name provided by the user.
    # print(msg)  # This line prints the greeting message to the console.
