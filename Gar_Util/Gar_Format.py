
"""
Gar_Format.py

This module provides functions for formatting numbers, dates, and phone numbers.

Functions:
- formatFloat(num, roundLen=2)
- formatInt(num)
- formatMoney(amount)
- formatPercent(num, roundLen=2)
- formatPhone(phone)
- dateShort(pDate)
- dateMedium(pDate)
- dateLong(pDate)
- dateShortWeekDay(pDate)
- dateLongWeekDay(pDate)

Author: Garrett Smith
Date: Nov 29, 2020
"""

# Imports
import datetime

# Constants
INT_FORMATTING = "{:,d}"
DATE_SHORT_FORMATTING = "%d/%m/%y"
DATE_MEDIUM_FORMATTING = "%d-%b-%y"
DATE_LONG_FORMATTING = "%d %B %Y"
DATE_SHORT_WEEKDAY = "%a, %d-%b-%y"
DATE_LONG_WEEKDAY = "%A, %B %d %Y"
# Functions


def formatFloat(num, roundLen=2):
    """
    Formats a floating-point number with the specified number of decimal places.

    Args:
        num (float): The number to be formatted.
        roundLen (int, optional): The number of decimal places to round to. Defaults to 2.

    Returns:
        str: The formatted number as a string.
    """
    floatTemp = "{:,." + str(roundLen) + "f}"
    return floatTemp.format(float(num))


def formatInt(num):
    """
    Formats an integer using the INT_FORMATTING pattern.

    Args:
        num (int): The integer to be formatted.

    Returns:
        str: The formatted integer.
    """
    return INT_FORMATTING.format(num)


def formatMoney(amount):
    """
    Formats the given amount as a money string.

    Args:
        amount (float): The amount to be formatted.

    Returns:
        str: The formatted money string.
    """
    return "$" + formatFloat(amount)


def formatPercent(num, roundLen=2):
    """
    Formats a number as a percentage string.

    Args:
        num (float): The number to be formatted as a percentage.
        roundLen (int, optional): The number of decimal places to round the percentage to. Defaults to 2.

    Returns:
        str: The formatted percentage string.
    """
    return formatFloat(num, roundLen) + "%"


def formatPhone(phone):
    """
    Formats a phone number by adding parentheses and dashes.

    Args:
        phone (str): The phone number to be formatted.

    Returns:
        str: The formatted phone number.
    """
    return "(" + phone[0:3] + ")" + phone[3:6] + "-" + phone[6:10]


def dateShort(pDate):
    """
    Formats the given date object into a short date string.

    Args:
        pDate (datetime.date): The date object to be formatted.

    Returns:
        str: The formatted short date string.
    """
    return pDate.strftime(DATE_SHORT_FORMATTING)


def dateMedium(pDate):
    """
    Formats the given date in medium format.

    Args:
        pDate (datetime): The date to be formatted.

    Returns:
        str: The formatted date string.
    """
    return pDate.strftime(DATE_MEDIUM_FORMATTING)


def dateLong(pDate):
    """
    Formats the given date in a long format.

    Args:
        pDate (datetime): The date to be formatted.

    Returns:
        str: The formatted date string.
    """
    return pDate.strftime(DATE_LONG_FORMATTING)


def dateShortWeekDay(pDate):
    """
    Returns the short weekday representation of the given date.

    Args:
        pDate (datetime): The date to format.

    Returns:
        str: The short weekday representation of the date.
    """
    return pDate.strftime(DATE_SHORT_WEEKDAY)


def dateLongWeekDay(pDate):
    """
    Returns the long weekday format of the given date.

    Args:
        pDate (datetime): The date to format.

    Returns:
        str: The long weekday format of the date.
    """
    return pDate.strftime(DATE_LONG_WEEKDAY)
