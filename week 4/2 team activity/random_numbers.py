"""
random_numbers.py
This program demonstrates generating random numbers and appending them to a list.
It contains two functions: main and append_random_numbers.
The main function creates a list and calls append_random_numbers to add random values.
The append_random_numbers function generates random numbers and adds them to a list.
"""

import random

def main():
    # Create a list with initial values
    numbers = [16.2, 75.1, 52.3]

    # Print the initial list
    print(f"Initial numbers list: {numbers}")

    # Call append_random_numbers with one argument to add one random number
    append_random_numbers(numbers)

    # Print the list after adding one random number
    print(f"Numbers list after adding one random number: {numbers}")

    # Call append_random_numbers with two arguments to add three random numbers
    append_random_numbers(numbers, 3)

    # Print the list after adding three random numbers
    print(f"Numbers list after adding three random numbers: {numbers}")


def append_random_numbers(numbers_list, quantity=1):
    """
    Append random numbers to a list.
    Parameters:
        numbers_list: The list to append random numbers to
        quantity: The quantity of random numbers to append (default: 1)
    Return: None
    """
    # Loop quantity times
    for _ in range(quantity):
        # Generate a random floating-point number between 0 and 100
        random_num = random.uniform(0, 100)

        # Round the number to one digit after the decimal
        rounded_num = round(random_num, 1)

        # Append the rounded random number to the list
        numbers_list.append(rounded_num)


# Call the main function if this file is executed
if __name__ == "__main__":
    main()
