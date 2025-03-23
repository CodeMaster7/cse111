from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction
import pytest

def test_water_column_height():
    """Verify that the water_column_height function works correctly.
    Parameters: none
    Return: nothing
    """
    height = water_column_height(0.0, 0.0)
    assert isinstance(height, float), "water_column_height must return a float"

    # Test case 1: tower_height = 0.0, tank_wall_height = 0.0
    assert water_column_height(0.0, 0.0) == 0.0

    # Test case 2: tower_height = 0.0, tank_wall_height = 10.0
    assert water_column_height(0.0, 10.0) == 7.5

    # Test case 3: tower_height = 25.0, tank_wall_height = 0.0
    assert water_column_height(25.0, 0.0) == 25.0

    # Test case 4: tower_height = 48.3, tank_wall_height = 12.8
    assert water_column_height(48.3, 12.8) == 57.9

def test_pressure_gain_from_water_height():
    """Verify that the pressure_gain_from_water_height function works correctly.
    Parameters: none
    Return: nothing
    """
    pressure = pressure_gain_from_water_height(0.0)
    assert isinstance(pressure, float), "pressure_gain_from_water_height must return a float"

    # Test case 1: height = 0.0
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)

    # Test case 2: height = 10.0
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)

    # Test case 3: height = 25.0
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    """Verify that the pressure_loss_from_pipe function works correctly.
    Parameters: none
    Return: nothing
    """
    pressure = pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75)
    assert isinstance(pressure, float), "pressure_loss_from_pipe must return a float"

    # Test case 1: pipe_diameter = 0.0, pipe_length = 0.0, friction_factor = 0.0, water_velocity = 0.0
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)

    # Test case 2: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)

    # Test case 3: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)

    # Test case 4: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)

    # Test case 5: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)

    # Test case 6: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)

    # Test case 7: pipe_diameter = 0.1, pipe_length = 100.0, friction_factor = 0.02, water_velocity = 1.0
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    """Verify that the pressure_loss_from_fittings function works correctly.
    Parameters: none
    Return: nothing
    """
    pressure = pressure_loss_from_fittings(1.65, 0)
    assert isinstance(pressure, float), "pressure_loss_from_fittings must return a float"

    # Test case 1: fluid_velocity = 0.0, quantity_fittings = 0.0
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)

    # Test case 2: fluid_velocity = 1.0, quantity_fittings = 1.0
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)

    # Test case 3: fluid_velocity = 1.0, quantity_fittings = 2.0
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)

    # Test case 4: fluid_velocity = 1.0, quantity_fittings = 5.0
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)

    # Test case 5: fluid_velocity = 1.0, quantity_fittings = 10.0
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    """Verify that the reynolds_number function works correctly.
    Parameters: none
    Return: nothing
    """
    reynolds = reynolds_number(0.048692, 1.75)
    assert isinstance(reynolds, float), "reynolds_number must return a float"

    # Test case 1: hydraulic_diameter = 0.048692, fluid_velocity = 0.00
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)

    # Test case 2: hydraulic_diameter = 0.048692, fluid_velocity = 1.65
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)

    # Test case 3: hydraulic_diameter = 0.048692, fluid_velocity = 1.75
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)

    # Test case 4: hydraulic_diameter = 0.286870, fluid_velocity = 1.65
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)

    # Test case 5: hydraulic_diameter = 0.286870, fluid_velocity = 1.75
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    """Verify that the pressure_loss_from_pipe_reduction function works correctly.
    Parameters: none
    Return: nothing
    """
    pressure = pressure_loss_from_pipe_reduction(0.286870, 1.75, 471729, 0.048692)
    assert isinstance(pressure, float), "pressure_loss_from_pipe_reduction must return a float"

    # Test case 1: larger_diameter = 0.28687, fluid_velocity = 0.00, reynolds_number = 1, smaller_diameter = 0.048692
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)

    # Test case 2: larger_diameter = 0.28687, fluid_velocity = 1.65, reynolds_number = 471729, smaller_diameter = 0.048692
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)

    # Test case 3: larger_diameter = 0.28687, fluid_velocity = 1.75, reynolds_number = 500318, smaller_diameter = 0.048692
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
