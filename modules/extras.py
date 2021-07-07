# xtra functions used throughout the entire game

# This function gets the string,splits and print it letter by letter using
# the sleep function from time library as the speedometer
def print_slow(str):
    from time import sleep
    from os import sys
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.04)

# This function checks if the answer is between the values that the system
# is waiting for. If not, returns a warning in portuguese and waits for
# the new answer.


def check_input(text, options):
    choice = int(input(text))

    while choice not in options:
        print_slow('Não entendi. Tente novamente.\n')
        choice = int(input(text))

    return choice

# This function checks if the answer is between the values that the system
# is waiting for. If not, returns a warning in english and waits for
# the new answer.


def check_input_en(text, options):
    choice = int(input(text))

    while choice not in options:
        print_slow('I could\'nt understand. Try again.\n')
        choice = int(input(text))

    return choice

# This function checks the OS and clears the terminal screen


def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
