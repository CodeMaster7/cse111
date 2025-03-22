from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_full_name function and verify that it returns a string.
    full_name = make_full_name("Sally", "Brown")
    assert isinstance(full_name, str), "make_full_name must return a string"

    # Test with regular names
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Robert", "Downey") == "Downey; Robert"
    assert make_full_name("John", "Lennon") == "Lennon; John"

    # Test with longer names
    assert make_full_name("Christopher", "Wellington") == "Wellington; Christopher"
    assert make_full_name("Elizabeth", "Montgomery") == "Montgomery; Elizabeth"

    # Test with short names
    assert make_full_name("Jo", "Li") == "Li; Jo"
    assert make_full_name("Ed", "Wu") == "Wu; Ed"

    # Test with hyphenated names
    assert make_full_name("Anna-Marie", "Smith") == "Smith; Anna-Marie"
    assert make_full_name("John", "Doe-Smith") == "Doe-Smith; John"
    assert make_full_name("Jean-Claude", "Van-Damme") == "Van-Damme; Jean-Claude"

def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Test with regular names
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Downey; Robert") == "Downey"
    assert extract_family_name("Lennon; John") == "Lennon"

    # Test with longer names
    assert extract_family_name("Wellington; Christopher") == "Wellington"
    assert extract_family_name("Montgomery; Elizabeth") == "Montgomery"

    # Test with short names
    assert extract_family_name("Li; Jo") == "Li"
    assert extract_family_name("Wu; Ed") == "Wu"

    # Test with hyphenated names
    assert extract_family_name("Smith; Anna-Marie") == "Smith"
    assert extract_family_name("Doe-Smith; John") == "Doe-Smith"
    assert extract_family_name("Van-Damme; Jean-Claude") == "Van-Damme"

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    # Test with regular names
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Downey; Robert") == "Robert"
    assert extract_given_name("Lennon; John") == "John"

    # Test with longer names
    assert extract_given_name("Wellington; Christopher") == "Christopher"
    assert extract_given_name("Montgomery; Elizabeth") == "Elizabeth"

    # Test with short names
    assert extract_given_name("Li; Jo") == "Jo"
    assert extract_given_name("Wu; Ed") == "Ed"

    # Test with hyphenated names
    assert extract_given_name("Smith; Anna-Marie") == "Anna-Marie"
    assert extract_given_name("Doe-Smith; John") == "John"
    assert extract_given_name("Van-Damme; Jean-Claude") == "Jean-Claude"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])