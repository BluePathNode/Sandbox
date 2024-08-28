import argparse

def view_command(option, argument):
    if option == '-o' and argument == 'login':
        print("Displaying login information")
    else:
        print(f"Unknown command: {option} {argument}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Command-line tool example")

    # Add command
    parser.add_argument('command', help="The command to run")

    # Add switches/flags (optional arguments)
    parser.add_argument('-o', '--option', help="Option switch", default=None)

    # Add argument (positional)
    parser.add_argument('argument', nargs='?', help="Argument for the command", default=None)

    # Parse arguments
    args = parser.parse_args()

    # Process the command
    if args.command == 'view':
        view_command(args.option, args.argument)
    else:
        print(f"Unknown command: {args.command}")

if __name__ == "__main__":
    main()
