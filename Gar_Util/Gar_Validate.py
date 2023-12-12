"""
Gar_Validate.py

This module provides functions for validating different types of data, such as integers, floats, strings, postal codes, phone numbers, etc.

Functions:
- validateInt(value, min=None, max=None)
- validatefloat(value, min=None, max=None)
- validateString(value, minLen=None, maxLen=None)
- validatePostalCode(value)
- validatePhone(value)
- validateYesNo(value)
- validateShortDate(value)
- validateProv(value)

Author: Garrett Smith
Date: Nov 29, 2020
"""

# Imports
import datetime

# Constants
PROV_LIST = ["ON", "QC", "NS", "NB", "MB", "BC",
             "PE", "SK", "AB", "NL", "NT", "YT", "NU"]

# Functions


def validateInt(value, min=None, max=None):
    """
    Validates if the given value is an integer within the specified range.

    Args:
        value (any): The value to be validated.
        min (int, optional): The minimum value allowed (inclusive). Defaults to None.
        max (int, optional): The maximum value allowed (inclusive). Defaults to None.

    Returns:
        bool: True if the value is a valid integer within the specified range, False otherwise.
    """
    try:
        number = int(value)
    except ValueError or TypeError:
        print("Value not an int.")
        return False
    else:
        if min != None and number < min:
            print("Value under min.")
            return False
        if max != None and number > max:
            print("Value over max.")
            return False
        else:
            return True


def validatefloat(value, min=None, max=None):
    """
    Validates if the given value is a float within the specified range.

    Args:
        value (float or str): The value to be validated.
        min (float, optional): The minimum value allowed. Defaults to None.
        max (float, optional): The maximum value allowed. Defaults to None.

    Returns:
        bool: True if the value is a valid float within the specified range, False otherwise.
    """
    try:
        number = float(value)
    except ValueError or TypeError:
        print("Value not a float.")
        return False
    else:
        if min != None and number < min:
            print("Value under min.")
            return False
        if max != None and number > max:
            print("Value over max.")
            return False

        return True


def validateString(value, minLen=None, maxLen=None):
    """
    Validates a string based on the given criteria.

    Args:
        value (str): The string to be validated.
        minLen (int, optional): The minimum length of the string. Defaults to None.
        maxLen (int, optional): The maximum length of the string. Defaults to None.

    Returns:
        bool: True if the string is valid, False otherwise.
    """
    if value == "":
        print("Value is empty.")
        return False
    elif maxLen != None and len(value) > maxLen:
        print("Value is too long.")
        return False
    elif minLen != None and len(value) < minLen:
        print("Value is too short.")
        return False
    else:
        return True


def validatePostalCode(value):
    """
    Validates a postal code.

    Args:
        value (str): The postal code to be validated.

    Returns:
        bool: True if the postal code is valid, False otherwise.
    """
    if len(value) != 6:
        print("Value is not the correct length(6).")
        return False
    if not value[1].isdigit() or not value[3].isdigit() or not value[5].isdigit():
        print("Value does not follow X0X0X0.")
        return False
    if not value[0].isalpha() or not value[2].isalpha() or not value[4].isalpha():
        print("Value does not follow X0X0X0.")
        return False
    else:
        return True


def validatePhone(value):
    """
    Validates a phone number.

    Args:
        value (str): The phone number to be validated.

    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    if len(value) != 10:
        print("Value is not the correct length(10).")
        return False
    elif not value.isdigit():
        print("Value is not all digits.")
        return False
    else:
        return True


def validateYesNo(value):
    """
    Validates if the input value is either 'Y' or 'N'.

    Args:
    value (str): The input value to be validated.

    Returns:
    bool: True if the value is 'Y' or 'N', False otherwise.
    """
    if value.upper() == "Y" or value.upper() == "N":
        return True
    else:
        print("Value is not Y or N.")
        return False


def validateShortDate(value):
    """
    Validates if the given value is a valid short date in the format YYYY-MM-DD.

    Args:
        value (str): The value to be validated.

    Returns:
        bool: True if the value is a valid short date, False otherwise.
    """
    if value == "":
        print("Value is empty.")
        return False
    else:
        try:
            datetime.datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            print("Value is not a valid date.")
            return False
        else:
            return True


def validateProv(value):
    """
    Validates if the given value is a valid province.

    Args:
        value (str): The value to be validated.

    Returns:
        bool: True if the value is a valid province, False otherwise.
    """
    if value.upper() in PROV_LIST:
        return True
    else:
        print("Value is not a valid province.")
        return False
