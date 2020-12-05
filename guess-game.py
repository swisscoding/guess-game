#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

import colored
import os
import random

# clears the previous stuff
os.system("clear" if os.name == "posix" else "cls")

# decoration
print(colored.stylize("\n---- | Guess the number | ----\n", colored.fg("red")))

# main program
try:
    # user interaction
    user_input_start = input("Do you want to start? ('y' to start; 'n' to quit): ")

    if user_input_start.lower() == "y":
        name = colored.stylize(input("\nWhat's your name?\n"), colored.fg("green"))
        print("\nSet the interval you want to use.")
        interval0, interval1 = int(input("From: ")), int(input("To: "))
        if interval0 > interval1:
            os.system("clear" if os.name == "posix" else "cls")
            print("Invalid Input\n")
            exit()

        # guesses count
        guesses = 0

        # random number in interval
        random_num = random.randint(interval0, interval1)

        print(colored.stylize("\n-------------------", colored.fg("red")))
        print(f"\nHello {name}! I am thinking of a number between {interval0} and {interval1}.\nTake a guess!\n")

        while True:
            user_guess = int(input(": "))
            if user_guess != random_num and user_guess in range(interval0, interval1+1):
                if user_guess > random_num:
                    print("Your guess is too high. Try again!\n")
                    guesses += 1
                elif user_guess < random_num:
                    print("Your guess is too low. Try again!\n")
                    guesses += 1
            elif user_guess == random_num:
                guesses += 1
                if guesses == 1:
                    print(f"Excellent job, {name}! You guessed my number in {guesses} guess!\n")
                else:
                    print(f"Excellent job, {name}! You guessed my number in {guesses} guesses!\n")
                exit()
            else:
                print("Number not in interval.\n")
    elif user_input_start.lower() == "n":
        os.system("clear" if os.name == "posix" else "cls")
        exit()
    else:
        os.system("clear" if os.name == "posix" else "cls")
        print("Invalid Input\n")
        exit()
except KeyboardInterrupt:
    os.system("clear" if os.name == "posix" else "cls")
    print("Game quitted\n")
    exit()
