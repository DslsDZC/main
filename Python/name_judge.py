import Terminal_function


def name_judge():
    try:
        name = input("Please enter your name: ").strip()
        key = input("Please enter the key of this studio: ").strip()
    except KeyboardInterrupt:
        print("KeyboardInterrupt: Program terminated.")
        return

    if name == 'DZC' and key == "200":
        print("Hello " + name + "!")
        print("Incorrect password!\nWelcome to the DZC terminal.")
        Terminal_function.welcome_words()
    elif name != 'DZC':
        print('Name input error')
    else:
        print("Incorrect password input")
