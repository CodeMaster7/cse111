"""
Author: Sam Bonfanti

Purpose: This program calculates the volume of a tire.

Problem:The size of a car tire in the United States is represented with three numbers like this: 205/60R15. The first number is the width of the tire in millimeters. The second number is the aspect ratio. The third number is the diameter in inches of the wheel that the tire fits. The volume of space inside a tire can be approximated with this formula:

v is the volume in liters,
π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
w is the width of the tire in millimeters,
a is the aspect ratio of the tire, and
d is the diameter of the wheel in inches.
"""
import math

# 1. ask the user for the width of the tire in millimeters
width = float(input("Enter the width of the tire in millimeters (ex 205): "))
# 2. ask the user for the aspect ratio of the tire
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
# 3. ask the user for the diameter of the wheel in inches
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))
# 4. calculate the volume of the tire using the formula
volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
# 5. round the volume to 2 decimal places
volume = round(volume, 2)
# 6. print the volume of the tire
print(f"The volume of the tire is {volume} liters.")
