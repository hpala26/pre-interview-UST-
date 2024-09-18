import pytest
from src.validate_passwords import validate_passwords

def test_valid_passwords():
    # Test with a valid password string
    input_passwords = "Passw0rd#,A1b@2c,D1e#2f3G"
    expected_output = "Passw0rd#,A1b@2c,D1e#2f3G"
    assert validate_passwords(input_passwords) == expected_output

def test_invalid_passwords():
    # Test with an invalid password string where none meet all criteria
    input_passwords = "123456,abcdef,ABCDEF"
    expected_output = "No valid passwords found."
    assert validate_passwords(input_passwords) == expected_output

def test_mixed_passwords():
    # Test with a mix of valid and invalid passwords
    input_passwords = "1234abcD#,A1@,abcdEFG,1A@bcd"
    expected_output = "1234abcD#,1A@bcd"
    assert validate_passwords(input_passwords) == expected_output

def test_empty_string():
    # Test with an empty string
    input_passwords = ""
    expected_output = "No valid passwords found."
    assert validate_passwords(input_passwords) == expected_output

def test_single_valid_password():
    # Test with a single valid password
    input_passwords = "Valid1@"
    expected_output = "Valid1@"
    assert validate_passwords(input_passwords) == expected_output

def test_single_invalid_password():
    # Test with a single invalid password
    input_passwords = "invalid1"
    expected_output = "No valid passwords found."
    assert validate_passwords(input_passwords) == expected_output
