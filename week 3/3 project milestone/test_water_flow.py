from pytest import approx
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe
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

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
