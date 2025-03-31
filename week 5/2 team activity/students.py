"""
Author: Sam Bonfanti

Purpose: A common task for many knowledge workers is to use a number, key,
or ID to look up information about a person. For example, a
knowledge worker may use a phone number or e-mail address as a key
to find (or look up) additional information about a customer.
During this activity, your team will write a Python program that
uses a student's I-Number to look up the student's name.

Problem: During this activity, your team will write a Python program that uses a student’s I-Number to look up the student’s name.

Core Requirements:
1) Open the students.csv file for reading, skip the first line of text in the file because it contains only headings, and read the other lines of the file into a dictionary. The program must store each student I-Number as a key and each I-Number name pair or each name as a value in the dictionary.
2) Get an I-Number from the user, use the I-Number to find the corresponding student name in the dictionary, and print the name.
3) If a user enters an I-Number that doesn’t exist in the dictionary, your program must print the message, "No such student" (without the quotes).

your program must include at least these 2 functions:
main
read_dictionary
"""
import csv

def main():
    # The column headings and indexes.
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    # Read the contents of a CSV file named students.csv
    # into a dictionary named students_dict. Use the I-Number
    # as the key in the dictionary.
    students_dict = read_dictionary("students.csv", I_NUMBER_INDEX)

    try:
        # Get an I-Number from the user.
        i_number = input("Enter an I-Number (xxxxxxxxx): ")

        # Remove dashes from the I-Number if present.
        i_number = i_number.replace("-", "")

        # Find the name that corresponds to the I-Number.
        value = students_dict[i_number]
        name = value[NAME_INDEX]

        # Print the name that corresponds to the I-Number.
        print(name)

    except KeyError as key_err:
        # This code will be executed if the user enters
        # an I-Number that doesn't exist in the dictionary.
        print()
        print(type(key_err).__name__, key_err)
        print(f"No such student: {i_number}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the students.csv file for reading and store a reference
    # to the opened file in a variable named text_file.
    with open(filename, "rt") as text_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(text_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so it should be skipped.
        next(reader)

        # Read the rest of the lines in the CSV file.
        for row_list in reader:
            # If the current row is not blank, add the
            # data from the current row to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                dictionary[key] = row_list


    # Return the dictionary that contains the lines of text.
    return dictionary

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()