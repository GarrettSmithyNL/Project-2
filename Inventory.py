def Inventory_Report():

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
    print()
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
        Description = ExspenseLst[4].strip()
        ItemQuantity = int(ExspenseLst[5].strip())
        ItemPrice = float(ExspenseLst[6].strip())

        
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


    # Progress bar column
    print()
    print(u'\u2500' * 77)
    print("Generating new column with updated inventory quantities...")
    print(u'\u2500' * 77)

    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=77, bar_format="{desc}  {bar}"):
        time.sleep(.1)


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

# Main function
def main():
    Inventory_Report()
# Running the program
main()
