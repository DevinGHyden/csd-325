# Name: Devin G. Hyden
# Date: 18 June 2026
# Assignment: Module 2.2 Assignment
# Purpose of Code: Created general code that included a function to test debugging tools

# import randint
from random import randint

def average(numbers):
    total = 0
    # loops through all numbers that were generated in main
    for num in numbers:
        # adds all the numbers together
        total += num
    # divides by the amount of numbers added together
    avg = total / len(numbers)
    return avg


def main():
    numbers = []
    # randomly generates an integer from 1 to 10, then appends them together in a list
    for _ in range(5):
        numbers.append(randint(1, 10))

    avg = average(numbers)
    # prints the list of numbers and the average
    print("Numbers: ", numbers)
    print("Average: ", avg)

if __name__ == "__main__":
    main()