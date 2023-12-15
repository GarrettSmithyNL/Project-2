
"""
Gar_Utility.py

This module contains utility functions for the Gar project.

Functions:
- exit(message=None)

Author: Garrett Smith
Date: Nov 29, 2020
"""
# Functions


def exit(message=None):
    """
    Function to prompt the user if they want to leave the program.

    Args:
        message (str, optional): The message to display if the user chooses to leave. Defaults to None.

    Returns:
        bool: True if the user chooses to leave, False otherwise.
    """
    while True:
        leaving = input("Would you like to leave? (Y/N): ").upper()
        if leaving == "":
            print("Please enter a valid input.")
        elif leaving == "Y" and message != None:
            print(message)
            return True
        elif leaving == "Y" and message == None:
            print("Thanks for using the program!")
            return True
        else:
            return False

