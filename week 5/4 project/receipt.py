"""
Author: Sam Bonfanti

Purpose: Prove that you can write a Python program that reads CSV files and creates, populates, and uses a dictionary.

Problem: A local grocery store subscribes to an online service that enables its customers to order groceries online. After a customer completes an order, the online service sends a CSV file that contains the customer's requests to the grocery store. The store needs you to write a program that reads the CSV file and prints to the terminal window a receipt that lists the purchased items and shows the subtotal, the sales tax amount, and the total.

Core Requirements:
- Print a welcome message to the program
- Print the product name, quantity, and price
- Print the total number of items purchased
- Print the subtotal, sales tax, and total
- Print a thank you message to the program
- Print a date and time to the program

Exceeding the Requirements:
- Added a countdown to New Year's Sale at the bottom of the receipt

your program must include at least these 2 functions:
main
read_dictionary
"""
import csv
from datetime import datetime, date
current_date_and_time = datetime.now()

def main():
    try:
        # The column headings and indexes for the products.csv file
        PRODUCT_NUM_INDEX = 0
        PRODUCT_NAME_INDEX = 1
        PRODUCT_PRICE_INDEX = 2
        SALES_TAX_RATE = 0.06

        # The column headings and indexes for the request.csv file
        REQUEST_PRODUCT_NUM_INDEX = 0
        REQUEST_QUANTITY_INDEX = 1

        # Initialize variables for totals
        total_items = 0
        subtotal = 0

        # Read the contents of a CSV file named products.csv
        # into a dictionary named products_dict. Use the product number
        # as the key in the dictionary.
        products_dict = read_dictionary("products.csv", PRODUCT_NUM_INDEX)

        # Define the file name
        request_filename = "request.csv"

        # Open the request.csv file for reading to check for invalid products first
        with open(request_filename, "rt") as request_file:
            # Use csv module to create a reader object
            reader = csv.reader(request_file)

            # Skip the first line of the CSV file because it contains column headings
            next(reader)

            # Check all product numbers in request file to make sure they exist
            for row_list in reader:
                product_num = row_list[REQUEST_PRODUCT_NUM_INDEX]
                # This will raise a KeyError if the product doesn't exist
                products_dict[product_num]

            # Print the store name at the top of the receipt
            print("Welcome to the Inkom Emporium")
            print()

        # If we get here, all products exist, so process the file
        with open(request_filename, "rt") as request_file:
            # Use csv module to create a reader object
            reader = csv.reader(request_file)

            # Skip the first line of the CSV file because it contains column headings
            next(reader)

            # Process each row in the request.csv file
            for row_list in reader:
                # Get the product number and quantity from the current row
                product_num = row_list[REQUEST_PRODUCT_NUM_INDEX]
                quantity = int(row_list[REQUEST_QUANTITY_INDEX])

                # Use the product number to find the corresponding item in products_dict
                product = products_dict[product_num]

                # Get the product name and price from the dictionary
                product_name = product[PRODUCT_NAME_INDEX]
                product_price = float(product[PRODUCT_PRICE_INDEX])

                # Print the product name, quantity, and price
                print(f"{product_name}: {quantity} @ ${product_price:.2f}")

                # Calculate the total number of items purchased
                total_items += quantity

                # Calculate subtotal for all items
                subtotal += product_price * quantity

            # Print a blank line
            print()

            # Print the total number of items purchased
            print(f"Number of items: {total_items}")

            # Print the subtotal due for all items
            print(f"Subtotal: ${subtotal:.2f}")

            # Calculate sales tax (moved outside the loop)
            sales_tax = subtotal * SALES_TAX_RATE

            # Print the sales tax
            print(f"Sales tax: ${sales_tax:.2f}")

            # Calculate total due (moved outside the loop)
            total_due = subtotal + sales_tax

            # Print the total amount of money due
            print(f"Total: ${total_due:.2f}")

            # Print a blank line
            print()

            # Print a thank you message
            print("Thank you for shopping at the Inkom Emporium.")

            # print date and time
            print(f"{current_date_and_time.strftime('%a %b %d %H:%M:%S %Y')}")

            # Print a blank line
            print()

            # Calculate and print the number of days until New Year
            new_year = date(current_date_and_time.year + 1, 1, 1)
            days_until_new_year = (new_year - current_date_and_time.date()).days
            print(f"New Year's (Jan 1st) Sale begins in {days_until_new_year} days! Don't miss out on our special discounts.")

    except FileNotFoundError as not_found_err:
        # This code will be executed if a file is not found
        print(f"Error: missing file")
        print(f"{not_found_err}")

    except KeyError as key_err:
        # Attempt to find the product ID,
        # which is not in the dictionary.
        print(f"Error: unknown product ID in the {request_filename} file")
        print(f"{key_err}")

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

# If this file was executed like this:
# > python receipt.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
