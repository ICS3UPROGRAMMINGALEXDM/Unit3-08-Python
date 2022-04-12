#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 04/11/2022
# Description: Calculates whether or not th year entered by the user
# is a leap year or not


def calculate():
    # if statement to check if the year is a leap year
    if main.year % 4 == 0:
        if main.year % 400 == 0:
            print("{} is a leap year!".format(main.year))
        elif main.year % 100 == 0:
            print("{} is not a leap year!".format(main.year))
        else:
            print("{} is a leap year!".format(main.year))
    else:
        print("{} is not a leap year!".format(main.year))


def main():

    restartLoop = True
    # loop is to ensure user can reenter values if previous were flagged
    while restartLoop:
        # Get user input
        main.year = input("Enter the year to be calculated: ")

        answerLoop = True
        try:
            # getting user input for year
            main.year = int(main.year)

            if main.year > 0:
                # call function calculate()
                calculate()

                # loop for error checking of answer
                while answerLoop:
                    # get user input
                    answer = (
                        input("Would you like to play again? (y/n): ").strip().lower()
                    )

                    if answer == "y":
                        print("Okay")
                        answerLoop = False
                    elif answer == "n":
                        print("Okay")
                        answerLoop = False
                        restartLoop = False
                    else:
                        print("I don't understand, please try again.")
            else:
                print("Please make sure to enter a number greater than 0")
        except ValueError:
            print("Ivalid input, try again!")


if __name__ == "__main__":
    main()
