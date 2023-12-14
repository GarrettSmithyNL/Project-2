# Comment

# Importing the libraries
import datetime
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Validate as validator

# Constants from Defaults.dat
try:
    DEFAULTS = open("defaults.dat", "r")
except FileNotFoundError:
    print("'defaults.dat' not found")
    exit()

NEXT_TRANSACTION = int(DEFAULTS.readline().strip())
NEXT_DRIVER = int(DEFAULTS.readline().strip())
MONTHLY_STAND_FEE = float(DEFAULTS.readline().strip())
DAILY_RENTAL_FEE = float(DEFAULTS.readline().strip())
WEEKLY_RENTAL_FEE = float(DEFAULTS.readline().strip())
HST_RATE = float(DEFAULTS.readline().strip())

DEFAULTS.close()

# Constants
TODAY_DATE = datetime.datetime.now()

# Defining Functions


# Opening Files
try:
    EMPLOYEE = open("Employee.dat", "r")
except FileNotFoundError:
    print("'Employee.dat' not found")
    exit()

try:
    EXPENSES = open("expenses.dat", "r")
except FileNotFoundError:
    print("'expenses.dat' not found")
    exit()

try:
    REVENUES = open("revenues.dat", "r")
except FileNotFoundError:
    print("'revenues.dat' not found")
    exit()

try:
    ITEM = open("item.dat", "r")
except FileNotFoundError:
    print("'item.dat' not found")
    exit()


# Main Loop
while True:
    # printing out the menu
    print(f"")
    print(f"HAB Taxi Services")
    print(f"Company Service System")
    print(f"")
    print(f"1. Enter a New Employee (driver).")
    print(f"2. Enter Company Revenues.")
    print(f"3. Enter Company Expenses.")
    print(f"4. Track Car Rental.")
    print(f"5. Record Employee Payment.")
    print(f"6. Print Company Finacial Listing.")
    print(f"7. Print Driver Finacial Listing.")
    print(f"8. Item On Hand Report")
    print(f"9. Exit")
    print(f"")
    print(f"Chose a number from the menu above.")

    # Gathering the input from the user
    while True:
        choice = input("Enter your choice: ")
        if validator.validateInt(choice, 1, 9):
            choice = int(choice)
            break

    # Processing the input from the user
    if choice == 1:
        print(f"Add a new employee.")
    elif choice == 2:
        print(f"Add a new revenue.")
    elif choice == 3:
        print(f"Add a new expense.")
    elif choice == 4:
        print(f"Track a car rental.")
    elif choice == 5:
        print(f"print record of employee payment.")
    elif choice == 6:
        print(f"print company financial listing.")
    elif choice == 7:
        print(f"print driver financial listing.")
    elif choice == 8:
        print(f"print item on hand report.")
    elif choice == 9:
        print(f"Exiting program.")
        break

# Closing Files
EMPLOYEE.close()
EXPENSES.close()
REVENUES.close()
ITEM.close()
