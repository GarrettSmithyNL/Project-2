# def inventory(item.dat, "expenses.dat"):    
# Program to generate a detailed report for the HAB taxi services company 
# to update their inventory and show the expensives of each driver.
# Written on: December 13, 2023
# Written by: Rodney Stead as part of Robot Group 9

# Import libraries
import datetime
CurDate = datetime.datetime.now()
import time
from tqdm import tqdm
from Gar_Util import Gar_Format as formater
from Gar_Util import Gar_Validate as validator

# Head column
print(u'\u2500' * 77)
print(f"HAB Taxi Services Inventory Report")
print(f"Report Date: {formater.dateInsurance(CurDate):<10}")
print()
print(f"Invoice  Invoice     Driver  Item  Item               Item    Item    Total   ")
print(f"Number   Date        Number   ID   Name               QTY   subtotal  Cost  ")
print(f"=============================================================================")

# Counters and accumulators
TaxiMtrCtr    = 0
NavSystemCtr  = 0
CleanSuppCtr  = 0
DriveLogCtr   = 0
FirstAidCtr   = 0
CarFreshnrCtr = 0
RepairCtr     = 0
InvoiceCtr    = 0
NewInvCtr     = 0

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
    ItemQuantity = int(ExspenseLst[4].strip())
    ItemPrice = float(ExspenseLst[5].strip())

    
#Processing and calculations

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
    InvoiceCtr    += 1
    NewInvCtr     += ItemQuantity

    TotSubtotal   += SubTotal
    TotalExpenses += ItemPrice

# Close expenses.dat file
f.close()

# Invoice Summary Column
print(f"=============================================================================")
print()
print(f"Total         QTY Items      Total        Total  ")
print(f"Invoices        Added       Subtotal     Expenses")
print(u'\u2500' * 51)
print(f":{formater.formatInt(InvoiceCtr):<3}          :{formater.formatInt(NewInvCtr):<3}          :{formater.formatMoney(TotSubtotal):<10}  :{formater.formatMoney(TotalExpenses):<10}")
print(u'\u2500' * 51)
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

# Closing column with progress bar
print()
print(u'\u2500' * 77)
print("Updating the item.dat file with the new inventory quantities...")
print(u'\u2500' * 77)
# Processing bar
for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=77, bar_format="{desc}  {bar}"):
    time.sleep(.1)


print(u'\u2500' * 77)
print("New item quantities have been successfully updated to item.dat file.")
print(u'\u2500' * 77)
print()

# Adding the new inventory to the item.dat file
# Opening the item.dat file to read the lines      
with open("item.dat", "r") as x:
    lines = x.readlines()

#Opening the item.dat file to write the new lines
with open("item.dat", "w") as x:
    for line in lines:
        ItemID, ItemName, PrevItemQty = line.strip().split(',')

        UpdatedItemQty = 0
        if ItemID == "001":
            UpdatedItemQty = TaxiMtrCtr
        elif ItemID == "002":
            UpdatedItemQty = NavSystemCtr
        elif ItemID == "003":
            UpdatedItemQty = CleanSuppCtr
        elif ItemID == "004":
            UpdatedItemQty = DriveLogCtr
        elif ItemID == "005":
            UpdatedItemQty = FirstAidCtr
        elif ItemID == "006":
            UpdatedItemQty = CarFreshnrCtr
        elif ItemID == "007":
            UpdatedItemQty = RepairCtr
        
        # Writing the new lines to the item.dat file     
        ItemID, ItemName, PrevItemQty = line.strip().split(',')   
        NewItemQty = int(PrevItemQty) + UpdatedItemQty
        x.write("{},{},{}\n".format(ItemID, ItemName, NewItemQty))

# Closing the item.dat file
x.close()  
          
# End of program


