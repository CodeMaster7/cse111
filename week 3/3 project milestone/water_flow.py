"""
Author: Sam Bonfanti

Purpose: This program calculates the water flow rate in a pipe.

Problem: Write a Python program that could help an engineer design a water distribution system. During this prove milestone, you will write three program functions and three test functions as described in the Steps section below.

Core Requirements:
1. all 3 functions test cases passed

formula for calculating the water column height.
h = t + 3w / 4
h is height of the water column
t is the height of the tower
w is the height of the walls of the tank that is on top of the tower

formula for calculating the pressure gain from water height.
P = ρgh / 1000
P is the pressure in kilopascals
ρ is the density of water 998.2 ( kilogram / meter3) *Just use # in your calculations
g is the acceleration from Earths gravity 9.80665 (meter / second2) *Just use # in your calculations
h is the height of the water column in meters

formula for calculating the pressure loss from pipe friction.
P = -fLρv^2 / 2000d
P is the lost pressure in kilopascals
f is the pipe's friction factor
L is the length of the pipe in meters
ρ is the density of water 998.2 (kilogram / meter3) *Just use # in your calculations
v is the velocity of the water flowing through the pipe in meters / second
d is the diameter of the pipe in meters

your program must include at least these 3 functions:
water_column_height
pressure_gain_from_water_height
pressure_loss_from_pipe
"""

import math

def water_column_height(tower_height, tank_height):
    """Calculate the height of a water column.

    Parameters:
        tower_height: the height of the tower in meters
        tank_wall_height: the height of the walls of the tank on top of the tower in meters

    Return: the height of the water column in meters
    """
    height = tower_height + (3 * tank_height) / 4
    return height

def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from water height.

    Parameters:
        height: the height of the water column in meters

    Return: the pressure gain from water height in kilopascals
    """
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, water_velocity):
    """Calculate the pressure loss from pipe friction.

    Parameters:
        pipe_diameter: the diameter of the pipe in meters
        pipe_length: the length of the pipe in meters
        friction_factor: the friction factor of the pipe
        water_velocity: the velocity of the water flowing through the pipe in meters / second

    Return: the pressure loss from pipe friction in kilopascals
    """

    # Calculate pressure loss using the formula: P = -fLρv^2 / 2000d
    pressure = -friction_factor * pipe_length * 998.2 * math.pow(water_velocity, 2) / (2000 * pipe_diameter)
    return pressure
