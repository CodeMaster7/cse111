"""
Author: Sam Bonfanti

Purpose: This program calculates the discount amount, sales tax amount, and total amount for a customer's purchase.

Problem:
You work for a retail store that wants to increase sales on Tuesday
and Wednesday, which are the store's slowest sales days. On Tuesday
and Wednesday, if a customer's subtotal is greater than $50, the
store will discount the customer's purchase by 10%.
"""


from datetime import datetime

# 1. ask the user for the subtotal
subtotal = float(input("Enter the subtotal: "))

# 2. get current day of the week from the computer operating system
day = datetime.now().weekday()

# Initialize discount to 0
discount = 0

# 3. if the subtotal is 50 or grater and today is Tuesday or Wednesday, subtract 10% from the subtotal
if subtotal >= 50 and (day == 1 or day == 2):
    discount = round(subtotal * 0.1, 2)
    subtotal = round(subtotal - discount, 2)

# 4. calculate the sales tax by multiplying the subtotal by 0.06
sales_tax = round(subtotal * 0.06, 2)

# 5. calculate the total amount by adding the sales tax to the subtotal
total = round(subtotal + sales_tax, 2)

# 6. print the discount amount (if applicable), sales tax amount, and total amount
if discount > 0:
    print(f"Discount amount: {discount:.2f}")
print(f"Sales tax amount: {sales_tax:.2f}")
print(f"Total amount: {total:.2f}")
