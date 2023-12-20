"""
This file contains the main code for the HAB Taxi project. It includes functions for managing expenses, generating reports, and performing various calculations related to revenue and expenses.

The code imports necessary libraries, reads default values from a file, defines supporting functions, and implements main functions such as printing profit listing report and cleaning up resources.

By: Garrett Smith, Rodnet Stead, Pavel Pliuiko, Shiva (Danny) Biera, Zachary Ropson
"""

# Importing the libraries
import datetime
import os
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


# Defining supporting functions


def cls():
    """
    Clears the console screen.

    This function clears the console screen by executing the appropriate command
    based on the operating system.

    By: Pavel Pliuiko
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def check_is_driver_exists(driver_number):
    """
    Check if a driver with the given driver number exists in the employees database.

    Args:
        driver_number (str): The driver number to check.

    Returns:
        bool: True if the driver exists, False otherwise.

    By: Pavel Pliuiko
    """
    for employee in employees:
        db_driver_number = employee.split(',')[0]

        if db_driver_number == driver_number:
            return True

    return False


def check_is_item_exists(item_number):
    """
    Check if an item with the given item number exists in the database.

    Parameters:
    item_number (str): The item number to check.

    Returns:
    bool: True if the item exists, False otherwise.

    By: Pavel Pliuiko
    """
    for item in items:
        db_item_number = item.split(',')[0]

        if db_item_number == item_number:
            return True

    return False


def check_is_item_quantity_enough(item_number, quantity):
    """
    Checks if the quantity of a given item is enough in the database.

    Parameters:
    item_number (str): The item number to check.
    quantity (int): The desired quantity of the item.

    Returns:
    bool: True if the quantity is enough, False otherwise.

    By: Pavel Pliuiko
    """
    for item in items:
        db_item_number = item.split(',')[0]
        db_item_quantity = int(item.split(',')[2])

        if db_item_number == item_number:

            if db_item_quantity >= quantity:
                return True
            return False

    print('Item not found!')
    return False


def generate_next_invoice_number():
    """
    Generates the next invoice number by reading the expenses.dat file and incrementing the last invoice number by 1.

    Returns:
        int: The next invoice number.

    By: Pavel Pliuiko
    """
    with open('expenses.dat', 'r') as f:
        lines = f.read().splitlines()
        return int(lines[-1].split(',')[0]) + 1


def get_item_cost(item_number):
    """
    Retrieves the cost of an item based on its item number.

    Parameters:
    item_number (str): The item number of the item.

    Returns:
    float: The cost of the item.

    By: Pavel Pliuiko
    """
    for item in items:
        db_item_number = item.split(',')[0]
        if db_item_number == item_number:
            return float(item.split(',')[3])


def add_expenses(invoice_number, date, driver_number, item_number, description, quantity, invoice_total, payment_method):
    """
    Add expenses to the expenses.dat file and update the item.dat file.

    Parameters:
    invoice_number (str): The invoice number.
    date (str): The date of the expense.
    driver_number (str): The driver number.
    item_number (str): The item number.
    description (str): The description of the item.
    quantity (int): The quantity of the item.
    invoice_total (float): The total amount of the invoice.
    payment_method (str): The payment method used.

    By: Pavel Pliuiko
    """
    with open('expenses.dat', 'a') as expenses:
        expenses.write(
            f'\n{invoice_number},{date},{driver_number},{item_number},{description},{quantity},{invoice_total},{payment_method}')

    for i, item in enumerate(items):
        db_item_number = item.split(',')[0]

        if db_item_number == item_number:
            item_description = item.split(',')[1]
            item_quantity = int(item.split(',')[2])
            item_price = item.split(',')[3]

            items[i] = f'{item_number},{item_description},{item_quantity - quantity},{item_price}'
            break

    with open('item.dat', 'w') as file:
        file.writelines(items)


# Defining Main Functions
def printProfitListing():
    """
    Prints the profit listing report based on user input for start and end dates.
    The report includes revenue details, expenses details, and calculates the total revenue,
    total expenses, and the profit or loss.

    By: Shiva (Danny) Biera
    """
    # Get user input for start and end dates
    while True:
        StDate = input("Enter the start date (YYYY-MM-DD): ")
        if validator.validateShortDate(StDate):
            StDate = datetime.datetime.strptime(StDate, "%Y-%m-%d")
            break

    while True:
        EndDate = input("Enter the end date (YYYY-MM-DD): ")
        if validator.validateShortDate(EndDate):
            EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
            break

    TodayDsp = datetime.datetime.strftime(TODAY_DATE, "%Y-%m-%d")

    print()
    print(
        f"HAB TAXI SERVICES                                                     #DATE : {TodayDsp:<10s}")
    print(f"PROFIT LISTING                              ")
    print()
    print(f"ENTER THE START DATE : {formater.dateInsurance(StDate):<10s}")
    print(f"ENTER THE END DATE   : {formater.dateInsurance(EndDate):<10s}")
    print("REVENUE DETAILS:")
    print()
    print("TRANSACTION    DRIVER      TRANSACTION     TRANSACTION        PAYMENT   AMOUNT      HST          TOTAL")
    print("    ID         NUMBER         DATE           DETAILS          METHOD")
    print("======================================================================================================")

    # Initialize counters and accumulators for summary / analytics.
    TotalRevAcc = 0

    # Open the file with the "r" mode for read.
    try:
        f = open("revenues.dat", "r")
    except FileNotFoundError:
        print("'revenues.dat' not found")
        exit()

    # Set up the loop to process all the records in the file.
    for RevenueRecord in f:
        # Input - read the first record and split into a list.
        RevenueLst = RevenueRecord.split(",")
        # Assign variables to each item in the list that are required in the report.
        # The .strip() method removes any spaces in the front or back of a value.

        TranID = RevenueLst[0].strip()
        DriNum = RevenueLst[1].strip()
        TranDate = datetime.datetime.strptime(
            RevenueLst[2].strip(), "%Y-%m-%d")
        # TranDateDsp = datetime.datetime.strptime(TranDate, "%Y-%m-%d")

        TranDetails = RevenueLst[3].strip()
        PayMethod = RevenueLst[7].strip()
        Amount = float(RevenueLst[4].strip())
        hstAmount = float(RevenueLst[5].strip())
        Total = float(RevenueLst[6].strip())

        # Calculations
        if StDate <= TranDate <= EndDate:
            print(f"{TranID:>3s}{DriNum:>16s}{formater.dateInsurance(TranDate):>18s}{TranDetails:>18s}{PayMethod:>13s}{formater.formatMoney(Amount):>10s}{formater.formatMoney(hstAmount):>11s}{formater.formatMoney(Total):>12s}")
            # Increment and Accumulate the summary / analytics data
            TotalRevAcc += Total

    # Close the file.
    f.close()
    # Print the summary / analytics data.
    print("======================================================================================================")
    print(
        f"                                                                           Total Revenue:    {formater.formatMoney(TotalRevAcc):>9s}")
    print()
    print("EXPENSES DETAILS:")
    print()
    print("INVOICE    INVOICE      DRIVER    DESCRIPTION            ITEM      QTY   COST        HST         TOTAL")
    print("NUMBER      DATE        NUMBER                           NUMBER")
    print("======================================================================================================")

    # Initialize counters and accumulators for summary / analytics.
    TotalExpAcc = 0

    # Open the file with the "r" mode for read.
    try:
        f = open("Expenses.dat", "r")
    except FileNotFoundError:
        print("'Expenses.dat' not found")
        exit()

    # Set up the loop to process all the records in the file.
    for ExpensesRecord in f:
        # Input - read the first record and split into a list.
        ExpensesLst = ExpensesRecord.split(",")

        # Assign variables to each item in the list that are required in the report.
        # The .strip() method removes any spaces in the front or back of a value.

        InvNum = ExpensesLst[0].strip()
        InvDate = datetime.datetime.strptime(
            ExpensesLst[1].strip(), "%Y-%m-%d")
        DrNum = ExpensesLst[2].strip()
        ItmNum = ExpensesLst[3].strip()
        DesCrp = ExpensesLst[4].strip()
        Qty = ExpensesLst[5].strip()
        TotalFE = float(ExpensesLst[6].strip())
        PayMethod = ExpensesLst[7].strip()

        # Calculations
        ExCost = TotalFE / 1.15
        ExHst = ExCost * 0.15

        if StDate <= InvDate <= EndDate:
            print(f"{InvNum:<4s}       {formater.dateInsurance(InvDate):<10s}   {DrNum:>4s}      {DesCrp:<20s}   {ItmNum:<3s}       {Qty:>2s} {formater.formatMoney(ExCost):>10s}    {formater.formatMoney(ExHst):>7s} {formater.formatMoney(TotalFE):>10s}")
            # Increment and Accumulate the summary / analytics data
            TotalExpAcc += TotalFE

    # Close the file.
    f.close()
    # Print the summary / analytics data.

    print("======================================================================================================")
    print(
        f"                                                                             Total Expenses: {formater.formatMoney(TotalExpAcc):>9s}")
    print()
    print()
    Balance = TotalRevAcc - TotalExpAcc
    print(
        f"                                                                              PROFIT or LOSS: {formater.formatMoney(Balance):>9s}")
    print()


def cleanup_and_exit():
    """
    Cleans up resources and exits the program.

    This function updates the defaults file with the current values of various variables,
    and closes all open file handles before exiting the program.

    Returns:
        bool: True indicating successful cleanup and exit.

    By: Zachary Ropson
    """
    print("Thanks for using the program.")
    # Updating the defaults file
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
    return True


def addExpense():
    """
    Function to add an expense record.

    This function prompts the user to enter various details of an expense, such as invoice date, driver number,
    item number, quantity, description, and payment method. It validates the input values and then generates
    the next invoice number. Finally, it prints the expense record and gives options to save, retry, or exit.

    By: Pavel Pliuiko
    """
    # Input and validate values
    while True:
        InvoiceDate = input('Enter invoice date (yyyy-mm-dd): ')
        if validator.validateShortDate(InvoiceDate):
            break

    while True:
        DriverNumber = input('Enter driver number: ')
        if check_is_driver_exists(DriverNumber):
            break
        else:
            print('Driver with that number doesnt exists!')

    while True:
        ItemNumber = input('Enter item number: ')
        if check_is_item_exists(ItemNumber):
            break

        print('Item with that number doesnt exists!')

    while True:
        Quantity = int(input('Enter quantity: '))
        if check_is_item_quantity_enough(ItemNumber):
            break
        else:
            print('Not enough product!')

    while True:
        Description = input('Enter description: ')
        if validator.validateString(Description):
            break

    while True:
        PaymentMethod = input('Enter payment method: ')
        if validator.validateString(PaymentMethod):
            break

    # Clear console
    cls()

    InvoiceNumber = generate_next_invoice_number()
    InvoiceTotal = float(Quantity) * get_item_cost(ItemNumber)

    # Print record
    print('Check the record: ')
    print()
    print('Invoice        Date        Driver        Item        Quantity        Invoice')
    print(' Number                    Number       Number                        Total')
    print('=============================================================================')
    print('{:<7}     {:<10}      {:<6}       {:<4}          {:<8}      {:<7}'
          .format(InvoiceNumber, InvoiceDate, DriverNumber, ItemNumber, Quantity, formater.formatMoney(InvoiceTotal)))
    print()

    NextAction = input('Type SAVE, RETRY or EXIT: ').upper()

    if NextAction == 'EXIT':
        return
    elif NextAction == 'SAVE':
        add_expenses(InvoiceNumber, InvoiceDate, DriverNumber, ItemNumber,
                     Description, Quantity, InvoiceTotal, PaymentMethod)
        cls()
        print('Record has saved!')
        print()
    elif NextAction == 'RETRY':
        cls()


def Inventory_Report():
    """
    Generates an inventory report for HAB Taxi Services.

    This function reads data from the "expenses.dat" file and calculates the inventory quantities and expenses.
    It then prints a detailed report of the inventory items, their quantities, and costs.
    Finally, it prints a summary of the total invoices, added quantities, subtotal, and total expenses.

    By: Rodney Stead
    """
    # Head column
    print(u'\u2500' * 77)
    print()
    print(f"HAB Taxi Services Inventory Report")
    print(f"Report Date: {formater.dateInsurance(TODAY_DATE):<10}")
    print()
    print(f"Invoice  Invoice     Driver  Item  Item               Item    Item    Total   ")
    print(f"Number   Date        Number   ID   Name               QTY   subtotal  Cost  ")
    print(f"=============================================================================")

    # Counters and accumulators
    TaxiMtrCtr = 0
    NavSystemCtr = 0
    CleanSuppCtr = 0
    DriveLogCtr = 0
    FirstAidCtr = 0
    CarFreshnrCtr = 0
    RepairCtr = 0
    InvoiceCtr = 0
    NewInvCtr = 0

    TotSubtotal = 0
    TotalExpenses = 0

    # Opening needed files
    f = open("expenses.dat", "r")

    for Exspenses in f:
        ExspenseLst = Exspenses.split(",")

        InvoiceNum = ExspenseLst[0].strip()
        InvoiceDate = ExspenseLst[1].strip()
        DriverNum = ExspenseLst[2].strip()
        ItemID = ExspenseLst[3].strip()
        Description = ExspenseLst[4].strip()
        ItemQuantity = int(ExspenseLst[5].strip())
        ItemPrice = float(ExspenseLst[6].strip())

    # Processing and calculations

        # Item name
        ItemName = ""
        if ItemID == "001":
            ItemName = "Taxi Meter"
            TaxiMtrCtr += ItemQuantity
        elif ItemID == "002":
            ItemName = "Navigation System"
            NavSystemCtr += ItemQuantity
        elif ItemID == "003":
            ItemName = "Cleaning Supplies"
            CleanSuppCtr += ItemQuantity
        elif ItemID == "004":
            ItemName = "Driver Log Book"
            DriveLogCtr += ItemQuantity
        elif ItemID == "005":
            ItemName = "First Aid Kit"
            FirstAidCtr += ItemQuantity
        elif ItemID == "006":
            ItemName = "Car Air Freshner"
            CarFreshnrCtr += ItemQuantity
        elif ItemID == "007":
            ItemName = "Repair Kit"
            RepairCtr += ItemQuantity

        # Subtotal
        SubTotal = (ItemPrice / 1.15) / ItemQuantity

        # Detail Line
        print(f"{InvoiceNum:<3}      {InvoiceDate:<10}  {DriverNum:<4}    {ItemID:<6}{ItemName:<17} {formater.formatInt(ItemQuantity):>2}     {formater.formatMoney(SubTotal):>7}   {formater.formatMoney(ItemPrice):>7}")

        # Update to counters and accumulators
        InvoiceCtr += 1
        NewInvCtr += ItemQuantity

        TotSubtotal += SubTotal
        TotalExpenses += ItemPrice

    # Close expenses.dat file
    f.close()

    # Opening item.dat file
    x = open("item.dat", "r")

    # Dictionary to update item quantities
    UpDatedQtyDic = {
        "001": TaxiMtrCtr,
        "002": NavSystemCtr,
        "003": CleanSuppCtr,
        "004": DriveLogCtr,
        "005": FirstAidCtr,
        "006": CarFreshnrCtr,
        "007": RepairCtr
    }
    for Items in x:
        ItemLst = Items.split(",")
        ItemNum = ItemLst[0].strip()
        PrevItemQty = int(ItemLst[2].strip())
        if ItemNum in UpDatedQtyDic:
            NewItemQty = UpDatedQtyDic[ItemNum] + PrevItemQty

        if ItemNum == "001":
            TaxiMtrCtr += int(PrevItemQty)
        elif ItemNum == "002":
            NavSystemCtr += int(PrevItemQty)
        elif ItemNum == "003":
            CleanSuppCtr += int(PrevItemQty)
        elif ItemNum == "004":
            DriveLogCtr += int(PrevItemQty)
        elif ItemNum == "005":
            FirstAidCtr += int(PrevItemQty)
        elif ItemNum == "006":
            CarFreshnrCtr += int(PrevItemQty)
        elif ItemNum == "007":
            RepairCtr += int(PrevItemQty)

    x.close()
    # Invoice Summary Column
    print(f"=============================================================================")
    print()
    print(f"Total         QTY Items      Total        Total  ")
    print(f"Invoices        Added       Subtotal     Expenses")
    print(u'\u2500' * 51)
    print(f":{formater.formatInt(InvoiceCtr):<3}          :{formater.formatInt(NewInvCtr):<3}          :{formater.formatMoney(TotSubtotal):<10}  :{formater.formatMoney(TotalExpenses):<10}")
    print(u'\u2500' * 51)

    print(u'\u2500' * 77)
    print("New inventory summary has been successfully generated.")
    print(u'\u2500' * 77)
    print()

    # Inventory Summary Column
    print(f"=============================================================================")
    print(f"New Inventory Summary")
    print(u'\u2500' * 28)
    print(f"Item Name          Added QTY")
    print(u'\u2500' * 28)
    print(f"Taxi Meters:             {formater.formatInt(TaxiMtrCtr):>3}")
    print(f"Navigation Systems:      {formater.formatInt(NavSystemCtr):>3}")
    print(f"Cleaning Supplies:       {formater.formatInt(CleanSuppCtr):>3}")
    print(f"Driver Log Books:        {formater.formatInt(DriveLogCtr):>3}")
    print(f"First Aid Kits:          {formater.formatInt(FirstAidCtr):>3}")
    print(f"Car Air Freshners:       {formater.formatInt(CarFreshnrCtr):>3}")
    print(f"Repair Kits:             {formater.formatInt(RepairCtr):>3}")
    print(u'\u2500' * 28)
    print(f"=============================================================================")


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
# By: Garrett Smith
if LAST_DATE_USED is not TODAY_DATE:
    # Getting the number of months since the last update
    numMonths = TODAY_DATE.month - LAST_DATE_USED.month
    # Going through the employees
    for lines in employees:
        # index = 0
        employee = lines.strip().split(",")
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
                f"{NEXT_TRANSACTION},{employee[0]},{formater.dateInsurance(TODAY_DATE.date())},Stand Fee,{amount},{tempHST},{tempTotal},Account\n")
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
                        f"{NEXT_TRANSACTION},{employee[0]},{formater.dateInsurance(TODAY_DATE)},Rental Fee,{amount},{tempHST},{tempTotal},Account\n")
                    writer.close()
                    # Updating the next transaction number
                    NEXT_TRANSACTION += 1
            # Setting the rental file pointer to the beginning
            rentals.seek(0)
    # Updating the Employee.dat file to add the charges to the account.
    employees.seek(0)

# Main Loop and menu
# By: Garrett Smith
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
        addExpense()
    elif choice == 4:
        print(f"Track a car rental.")
    elif choice == 5:
        print(f"print record of employee payment.")
    elif choice == 6:
        printProfitListing()
    elif choice == 7:
        print(f"print driver financial listing.")
    elif choice == 8:
        Inventory_Report()
    elif choice == 9:
        if cleanup_and_exit():
            break
