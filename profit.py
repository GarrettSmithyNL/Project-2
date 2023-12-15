
# Comment like a pro.
# Import any required libraries
import Gar_Util
import datetime
from Gar_Util import Gar_Format as FV
from Gar_Util import Gar_Validate as VD








# Get user input for start and end dates
StDate = input("Enter the start date (YYYY-MM-DD): ")
StDateDsp = datetime.datetime.strptime(StDate, "%Y-%m-%d")
EndDate = input("Enter the end date (YYYY-MM-DD): ")
EndDateDsp = datetime.datetime.strptime(EndDate, "%Y-%m-%d")




Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%Y-%m-%d")

print()
print()
print()

print()
print(f"HAB TAXI SERVICES                                                                    #DATE : {TodayDsp:<10s}")
print(f"PROFIT LISTING                              ")
print()
print("PLEASE ENTER THE STARTING AND ENDING DATES INORDER TO GET PROFIT/LOSS REPORT FOR THAT PERIOD")
print()
print(f"ENTER THE START DATE : {StDate:<10s}")
print(f"ENTER THE END DATE   : {EndDate:<10s}")

print("REVENUE DETAILS:")
print()
print()
print()

print("TRANSACTION    DRIVER      TRANSACTION     TRANSACTION        PAYMENT   AMOUNT      HST          TOTAL")
print("    ID         NUMBER         DATE           DETAILS          METHOD")
print("======================================================================================================")
print()

# Initialize counters and accumulators for summary / analytics.

TotalRevAcc = 0

# Open the file with the "r" mode for read.
f = open("Revenues.dat", "r")


# Set up the loop to process all the records in the file.
for RevenueRecord in f:      
    # Input - read the first record and split into a list.
    RevenueLst = RevenueRecord.split(",")
    
    
   
   
    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    
    TranID = RevenueLst[0].strip()
    DriNum = RevenueLst[1].strip()
    TranDate = RevenueLst[2].strip()
    #TranDateDsp = datetime.datetime.strptime(TranDate, "%Y-%m-%d")
    
    TranDetails = RevenueLst[3].strip()
    PayMethod = RevenueLst[7].strip()
    Amount = float(RevenueLst[4].strip())
    HST = float(RevenueLst[5].strip())
    Total = float(RevenueLst[6].strip())
    
    #Calculations
    if StDate <=TranDate<= EndDate:
        
        
        
                
        print(f"{TranID:>3s}           {DriNum:>5s}        {TranDate:<10s}      {TranDetails:<12s}    {PayMethod:>4s}    {FV.formatMoney(Amount):>9s}  {FV.formatMoney(HST):>9s}{FV.formatMoney(Total):>12s}")
        # Increment and Accumulate the summary / analytics data
        TotalRevAcc += Total
      
    
    
    
    
# Close the file.
f.close()
# Print the summary / analytics data.
print("======================================================================================================")


print(f"                                                                           Total Revenue:    {FV.formatMoney(TotalRevAcc):>9s}")
print()
print()
print()
print()
print("EXPENSES DETAILS:")
print()
print()
print()

print("INVOICE    INVOICE      DRIVER    DESCRIPTION            ITEM      QTY   COST        HST         TOTAL")
print("NUMBER      DATE        NUMBER                           NUMBER")

print("======================================================================================================")
print()

# Initialize counters and accumulators for summary / analytics.
TotalExpAcc = 0


# Open the file with the "r" mode for read.
f = open("Expenses.dat", "r")


# Set up the loop to process all the records in the file.
for ExpensesRecord in f:      
    # Input - read the first record and split into a list.
    ExpensesLst = ExpensesRecord.split(",")

    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    
    InvNum = ExpensesLst[0].strip()
    InvDate =ExpensesLst[1].strip()
    DrNum =ExpensesLst[2].strip()
    ItmNum =ExpensesLst[3].strip()
    '''PayMethod = "CASH"''' 
    Qty = ExpensesLst[5].strip()
    DesCrp =ExpensesLst[4].strip()
    TotalFE = float(ExpensesLst[6].strip())
    
    #Calculations
    ExCost = TotalFE / 1.15
    ExHst = ExCost * 0.15
    
    
    if StDate <=InvDate<= EndDate:
    
        print(f"{InvNum:<4s}       {InvDate:<10s}   {DrNum:>4s}      {DesCrp:<20s}   {ItmNum:<3s}       {Qty:>2s} {FV.formatMoney(ExCost):>10s}    {FV.formatMoney(ExHst):>7s} {FV.formatMoney(TotalFE):>10s}")
        # Increment and Accumulate the summary / analytics data
        TotalExpAcc += TotalFE
        
# Close the file.
f.close()
# Print the summary / analytics data.

print("======================================================================================================")

print(f"                                                                             Total Expenses: {FV.formatMoney(TotalExpAcc):>9s}")

print()
print()

Balance = TotalRevAcc - TotalExpAcc
print(f"                                                                              PROFIT (LOSS): {FV.formatMoney(Balance):>9s}")

print()

