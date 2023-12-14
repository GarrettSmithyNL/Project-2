# Comment

# Importing the libraries
import datetime
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Validate as validator

# Constants from Defaults.dat
try:
    defaults = open("defaults.dat", "r")
except FileNotFoundError:
    print("'defaults.dat' not found")
    exit()

NEXT_TRANSACTION = int(defaults.readline().strip())
NEXT_DRIVER = int(defaults.readline().strip())
MONTHLY_STAND_FEE = float(defaults.readline().strip())
DAILY_RENTAL_FEE = float(defaults.readline().strip())
WEEKLY_RENTAL_FEE = float(defaults.readline().strip())
HST_RATE = float(defaults.readline().strip())
LAST_DATE_USED = datetime.datetime.strptime(
    defaults.readline().strip(), "%Y-%m-%d")

defaults.close()
# Constants
TODAY_DATE = datetime.datetime.now()
LAST_MONTH = TODAY_DATE.month - 1


# Defining Functions


# Opening Files
try:
    employees = open("Employee.dat", "r")
except FileNotFoundError:
    print("'Employee.dat' not found")
    exit()

try:
    expenses = open("expenses.dat", "r")
except FileNotFoundError:
    print("'expenses.dat' not found")
    exit()

try:
    revenues = open("revenues.dat", "r")
except FileNotFoundError:
    print("'revenues.dat' not found")
    exit()

try:
    items = open("item.dat", "r")
except FileNotFoundError:
    print("'item.dat' not found")
    exit()

try:
    rentals = open("rentals.dat", "r")
except FileNotFoundError:
    print("'rentals.dat' not found")
    exit()

# Updating file, This is definitly not "Automatic"
if LAST_DATE_USED is not TODAY_DATE:
    # Getting the number of months since the last update
    numMonths = TODAY_DATE.month - LAST_DATE_USED.month
    print(numMonths)
    # Going through the employees
    for lines in employees:
        # index = 0
        employee = lines.strip().split(",")
        print(employee)
        # Checking if the employee is a car owner
        if employee[10].upper() == "OWN":
            # Calculating the amount to be paid
            amount = MONTHLY_STAND_FEE * numMonths
            tempHST = amount * HST_RATE
            tempTotal = amount + tempHST
            # Updating the employee's record
            employee[9] = str(float(employee[9]) + tempTotal)
            # Appending a new transaction to the revenues file
            writer = open("revenues.dat", "a")
            writer.write(
                f"{NEXT_TRANSACTION},{employee[0]},{formater.dateInsurance(TODAY_DATE.date())},Stand Fee,{amount},{tempHST},{tempTotal}\n")
            writer.close()
            # Updating the next transaction number
            NEXT_TRANSACTION += 1
        elif employee[10].upper() == "RENT":
            for rental in rentals:
                rents = rental.strip().split(",")
                rentDate = datetime.datetime.strptime(
                    rents[2].strip(), "%Y-%m-%d")
                # Checking if the employee has rented a car since the last update
                if rents[1] == employee[0] and rentDate.month >= TODAY_DATE.month - numMonths:
                    # Calculating the amount to be paid
                    if rents[5] == 7:
                        amount = WEEKLY_RENTAL_FEE
                    else:
                        amount = DAILY_RENTAL_FEE * int(rents[5])
                    tempHST = amount * HST_RATE
                    tempTotal = amount + tempHST
                    # Updating the employee's record
                    employee[9] = str(float(employee[9]) + tempTotal)
                    # Appending a new transaction to the revenues file
                    writer = open("revenues.dat", "a")
                    writer.write(
                        f"{NEXT_TRANSACTION},{employee[0]},{formater.dateInsurance(TODAY_DATE)},Rental Fee,{amount},{tempHST},{tempTotal}\n")
                    writer.close()
                    # Updating the next transaction number
                    NEXT_TRANSACTION += 1
            rentals.seek(0)
        # Updating the employee file
        # empNum = employee[0]
        # empName = employee[1]
        # empAddress = employee[2]
        # empCity = employee[3]
        # empPhone = employee[4]
        # empDLNum = employee[5]
        # empStartDate = employee[6]
        # empInsurComp = employee[7]
        # empInsurNum = employee[8]
        # empInsurExp = employee[9]
        # empCarStatus = employee[10]

        # writer = open("Employee.dat", "w")
        # for employee in writer:
        #     if employee[0] == empNum:
        #         employee.write(
        #             f"{empNum},{empName},{empAddress},{empCity},{empPhone},{empDLNum},{empStartDate},{empInsurComp},{empInsurNum},{empInsurExp},{empCarStatus}")
        # writer.close()
        # index += 1
    employees.seek(0)
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
        NEXT_DRIVER += 1
        print(f"Driver ID: {NEXT_DRIVER}")
    elif choice == 2:
        print(f"Add a new revenue.")
    elif choice == 3:
        print(f"Add a new expense.")
        NEXT_TRANSACTION += 1
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


# Updating Defaults.dat
defaults.close()

defaults = open("defaults.dat", "w")
defaults.write(str(NEXT_TRANSACTION) + "\n")
defaults.write(str(NEXT_DRIVER) + "\n")
defaults.write(str(MONTHLY_STAND_FEE) + "\n")
defaults.write(str(DAILY_RENTAL_FEE) + "\n")
defaults.write(str(WEEKLY_RENTAL_FEE) + "\n")
defaults.write(str(HST_RATE) + "\n")
defaults.write(str(TODAY_DATE.date()) + "\n")
defaults.close()


employees.close()
expenses.close()
revenues.close()
items.close()
rentals.close()
