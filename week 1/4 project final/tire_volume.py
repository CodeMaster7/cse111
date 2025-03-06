# author: Sam Bonfanti

# purpose: This program calculates the volume of a tire and stores the information in a text file.

# Purpose: Prove that you can write a Python program that calls functions and methods to get the current date and to append values to a text file.

# stretch challenge: After your program prints the tire volume to the terminal window, your program should ask the user if she wants to buy tires with the dimensions that she entered. If the user answers "yes", your program should ask for her phone number and store her phone number in the volumes.txt file. If the user answers "no", your program should print "Thank you for considering us for your tire purchase."

import math
from datetime import datetime

# current date no time
current_date = datetime.now().strftime('%Y-%m-%d')

# 1. ask the user for the width of the tire in millimeters
# Using int() to work with whole numbers only
width = int(input("Enter the width of the tire in millimeters (ex 205): "))
# 2. ask the user for the aspect ratio of the tire
# Using int() to work with whole numbers only
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
# 3. ask the user for the diameter of the wheel in inches
# Using int() to work with whole numbers only
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))
# 4. calculate the volume of the tire using the formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
# 5. round the volume to 2 decimal places
volume = round(volume, 2)
# Format volume to remove trailing zeros if it's a whole number
volume_str = str(int(volume)) if volume.is_integer() else str(volume)
# 6. print the volume of the tire
print(f"The volume of the tire is {volume_str} liters.")

# 7. ask the user if she wants to buy tires with the dimensions that she entered
buy_tires = input("Would you like to buy tires with these dimensions? (yes/no): ")

# Open the text file named volumes.txt in append mode
with open("volumes.txt", "at") as volumes_file:
    # 8. if the user answers "yes", ask for her phone number and store her phone number in the volumes.txt file
    if buy_tires.lower() == "yes":
        phone_number = input("Enter your phone number: ")
        # Print the current date, width, aspect ratio, diameter, volume, and phone number
        print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_str}, {phone_number}", file=volumes_file)
    else:
        # If the user doesn't want to buy tires, just record the tire information without phone number
        print(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume_str}", file=volumes_file)

        # 9. if the user answers "no", print "Thank you for considering us for your tire purchase."
        if buy_tires.lower() == "no":
            print("Thank you for considering us for your tire purchase.")