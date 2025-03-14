"""
Author: Sam Bonfanti

Purpose: This program computes and prints the storage efficiency for each of the following 12 steel can sizes. Then visually examines the output and answers the question, "Which can size has the highest storage efficiency?"

Problem: In many countries, food is stored in steel cans (also known as tin cans) that are shaped like cylinders. There are many different sizes of steel cans. The storage efficiency of a can tells us how much a can stores versus how much steel is required to make the can. Some sizes of cans require a lot of steel to store a small amount of food. Other sizes of cans require less steel and store more food. A can size with a large storage efficiency is considered more friendly to the environment than a can size with a small storage efficiency.

Core Requirements:
1. Your program must compute the volume of all 12 can sizes.
2. Your program must compute the surface area of all 12 can sizes.
3. Your program must compute and print the storage efficiency of all 12 can sizes.

your program include at least these three functions:
main
compute_volume
compute_surface_area
"""

# Import the standard math module so that
# math.pi can be used in this program.
import math
# Define the main function.
def main():
    # Define the variables for the can sizes.
    can_sizes = [
        {"name": "#1 Picnic", "radius": 6.83, "height": 10.16, "cost": 0.28},
        {"name": "#1 Tall", "radius": 7.78, "height": 11.91, "cost": 0.43},
        {"name": "#2", "radius": 8.73, "height": 11.59, "cost": 0.45},
        {"name": "#2.5", "radius": 10.32, "height": 11.91, "cost": 0.61},
        {"name": "#3 Cylinder", "radius": 10.79, "height": 17.78, "cost": 0.86},
        {"name": "#5", "radius": 13.02, "height": 14.29, "cost": 0.83},
        {"name": "#6Z", "radius": 5.40, "height": 8.89, "cost": 0.22},
        {"name": "#8Z short", "radius": 6.83, "height": 7.62, "cost": 0.26},
        {"name": "#10", "radius": 15.72, "height": 17.78, "cost": 1.53},
        {"name": "#211", "radius": 6.83, "height": 12.38, "cost": 0.34},
        {"name": "#300", "radius": 7.62, "height": 11.27, "cost": 0.38},
        {"name": "#303", "radius": 8.10, "height": 11.11, "cost": 0.42},
    ]
    # Compute and print the storage efficiency for all 12 can sizes.
    for can in can_sizes:
        # Calculate the volume
        volume = compute_volume(can["radius"], can["height"])

        # Calculate the surface area
        surface_area = compute_surface_area(can["radius"], can["height"])

        # Calculate the storage efficiency
        storage_efficiency = compute_storage_efficiency(volume, surface_area)

        # Print the name of the can and its storage efficiency
        print(f"{can['name']}: {storage_efficiency:.2f}")

# Define the compute_volume function.
def compute_volume(radius, height):
    """Compute and return the volume of a cylinder.
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the volume of the cylinder
    """
    volume = math.pi * radius**2 * height
    return volume

# Define the compute_surface_area function.
def compute_surface_area(radius, height):
    """Compute and return the surface area of a cylinder.
    Parameters
    radius: the radius of the cylinder
    height: the height of the cylinder
    Return: the surface area of the cylinder
    """
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

# Define the compute_storage_efficiency function.
def compute_storage_efficiency(volume, surface_area):
    """Compute and return the storage efficiency.
    Parameters
    volume: the volume of the cylinder
    surface_area: the surface area of the cylinder
    Return: the storage efficiency
    """
    storage_efficiency = volume / surface_area
    return storage_efficiency

# Call the main function so that
# this program will start executing.
main()
