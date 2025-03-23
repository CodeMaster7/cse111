"""
Author: Sam Bonfanti

Purpose: This program calculates the water flow rate in a pipe.

Problem: Write a Python program that could help an engineer design a water distribution system. During this prove milestone, you will write 7 program functions and 6 test functions as described in the Steps section below.

Core Requirements:
1. all 6 functions test cases passed

your program must include at least these 3 functions:
main
water_column_height
pressure_gain_from_water_height
pressure_loss_from_pipe
pressure_loss_from_fittings
reynolds_number
pressure_loss_from_pipe_reduction
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

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    """Calculate the pressure loss from fittings.

    Parameters:
        fluid_velocity: the velocity of the fluid in meters / second
        quantity_fittings: the number of fittings in the pipe

    Return: the pressure loss from fittings in kilopascals
    """

    # Calculate pressure loss using the formula: P = -0.04 * 998.2 * math.pow(fluid_velocity, 2) * quantity_fittings / 2000
    pressure = -0.04 * 998.2 * math.pow(fluid_velocity, 2) * quantity_fittings / 2000
    return pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Calculate the Reynolds number.

    Parameters:
        hydraulic_diameter: the hydraulic diameter of the pipe in meters
        fluid_velocity: the velocity of the fluid in meters / second

    Return: the Reynolds number
    """

    # Calculate Reynolds number using the formula: R = ρdv / μ
    reynolds = 998.2 * hydraulic_diameter * fluid_velocity / 0.0010016
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """Calculate the pressure loss from pipe reduction.

    Parameters:
        larger_diameter: the diameter of the larger pipe in meters
        fluid_velocity: the velocity of the fluid in meters / second
        reynolds_number: the Reynolds number
        smaller_diameter: the diameter of the smaller pipe in meters

    Return: the pressure loss from pipe reduction in kilopascals
    """

    # Calculate pressure loss using the formula: k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ^ 4 - 1)
    k = (0.1 + 50 / reynolds_number) * (math.pow((larger_diameter / smaller_diameter), 4) - 1)
    pressure = -k * 998.2 * math.pow(fluid_velocity, 2) / 2000
    return pressure

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
