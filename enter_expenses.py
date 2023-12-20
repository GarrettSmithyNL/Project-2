# Import libraries
import os

from Gar_Util.Gar_Format import formatMoney
from Gar_Util.Gar_Validate import validateShortDate

# Opening needed files
employees = open("Employee.dat", "r")
items = open("item.dat", "r")

employees_list = employees.readlines()
items_list = items.readlines()

employees.close()
items.close()


# Define functions

# Clear console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_is_driver_exists(driver_number):
    for employee in employees_list:
        db_driver_number = employee.split(',')[0]

        if db_driver_number == driver_number:
            return True

    return False


def check_is_item_exists(item_number):
    for item in items_list:
        db_item_number = item.split(',')[0]

        if db_item_number == item_number:
            return True

    return False


def check_is_item_quantity_enough(item_number, quantity):
    for item in items_list:
        db_item_number = item.split(',')[0]
        db_item_quantity = int(item.split(',')[2])

        if db_item_number == item_number:

            if db_item_quantity >= quantity:
                return True
            return False

    print('Item not found!')
    return False


def generate_next_invoice_number():
    with open('expenses.dat', 'r') as f:
        lines = f.read().splitlines()

        return int(lines[-1].split(',')[0]) + 1


def get_item_cost(item_number):
    for item in items_list:
        db_item_number = item.split(',')[0]

        if db_item_number == item_number:
            return float(item.split(',')[3])


# Save add new record to expenses and change items
def add_expenses(invoice_number, date, driver_number, item_number, quantity, invoice_total):
    with open('expenses.dat', 'a') as expenses:
        expenses.write(
            f'\n{invoice_number},{date},{driver_number},{item_number},{quantity},{invoice_total}')

    for i, item in enumerate(items_list):
        db_item_number = item.split(',')[0]

        if db_item_number == item_number:
            item_description = item.split(',')[1]
            item_quantity = int(item.split(',')[2])
            item_price = item.split(',')[3]

            items_list[i] = f'{item_number},{item_description},{item_quantity - quantity},{item_price}'
            break

    with open('item.dat', 'w') as file:
        file.writelines(items_list)


while True:

    # Input and validate values
    while True:
        InvoiceDate = input('Enter invoice date (yyyy-mm-dd): ')

        if validateShortDate(InvoiceDate):
            break

    while True:
        DriverNumber = input('Enter driver number: ')

        if check_is_driver_exists(DriverNumber):
            break

        print('Driver with that number doesnt exists!')

    while True:
        ItemNumber = input('Enter item number: ')

        if check_is_item_exists(ItemNumber):
            break

        print('Item with that number doesnt exists!')

    while True:
        Quantity = int(input('Enter quantity: '))

        if check_is_item_quantity_enough(ItemNumber, Quantity):
            break

        print('Not enough product!')

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
        break
    elif NextAction == 'SAVE':
        add_expenses(InvoiceNumber, InvoiceDate, DriverNumber,
                     ItemNumber, Quantity, InvoiceTotal)
        cls()
        print('Record has saved!')
        print()
    elif NextAction == 'RETRY':
        cls()
