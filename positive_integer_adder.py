# !/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program adds all positive integers together


def main():
    # counter and answer
    answer = 0
    counter = 0
    positive_integer = 0

    # input
    loop_number = int(input("Enter the number of integers you want to add: "))

    # loop & process & output
    while counter < loop_number:
        positive_integer = int(input("Enter a number: "))
        counter = counter + 1
        if positive_integer < 0:
            continue
        else:
            answer = answer + positive_integer
    print("The sum of all positive integers is {}".format(answer))


if __name__ == "__main__":
    main()
