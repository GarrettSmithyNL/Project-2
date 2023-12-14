
# Comment like a pro.
# Import any required libraries
import Format as FV
import validations as VD







import datetime
Today = datetime.datetime.now()
TodayDsp = datetime.datetime.strftime(Today, "%Y-%m-%d")
# Define any program constants (Maybe in a file)
# Process to follow when generating a report.
# Print main headings and column headings.
"""print()
print("HAB TAXI SERVICES                                  DRIVER NUMBER:      {:>4s}")
print(f"YEARLY PROFIT LISTING                              DATE         : {TodayDsp:<10s}")
print()
print("RENTAL DETAILS:")
print()

print("START       END          CAR       RENTAL      RENTAL       NUM OF     HST")
print("DATE        DATE         NUMBER    TYPE        COST         DAYS          ")
print("=================================================================================")


# Initialize counters and accumulators for summary / analytics.
CustOverCtr = 0
PayDueAcc = 0
# Open the file with the "r" mode for read.
f = open("CustExtra.dat", "r")
# Set up the loop to process all the records in the file.
for CustRecord in f:      
    # Input - read the first record and split into a list.
    CustLst = CustRecord.split(",")
   
    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    CustNum = CustLst[0].strip()
    CustName = CustLst[1].strip()
    Phone = CustLst[2].strip()
    BalDue = float(CustLst[3].strip())
    CredLim = float(CustLst[4].strip())
    NextPayDate = CustLst[9].strip()
    NextPayDate = datetime.datetime.strptime(NextPayDate, "%Y-%m-%d")
    # For an exception report, place an if before the calculations that defines the exception.
    if BalDue > CredLim:
        # Perform any required calculations.  In this report, none are necessary.
        AmtOver = BalDue - CredLim
        PayDue = (CredLim * .05) + AmtOver
        # Print the detail line.  A detail line is the details of the record you want.
        NextPayDateDsp = datetime.datetime.strftime(NextPayDate, "%Y-%m-%d")
        print(f"{CustNum:<6s} {CustName:<20s} {Phone:>12s}  {FV.FDollar2(CredLim):>9s} {FV.FDollar2(AmtOver):>9s}  {NextPayDateDsp:>12s}  {FV.FDollar2(PayDue):>9s}")
        # Increment and Accumulate the summary / analytics data.
        CustOverCtr += 1
        PayDueAcc += PayDue
# Close the file.
f.close()
# Print the summary / analytics data.
print("======================================================================================")
print(f"Total customers: {CustOverCtr:>3d}                                                        {FV.FDollar2(PayDueAcc):>10s}")
print()

"""

print()
print()
print()
print()



print("REVENUE DETAILS:")
print()
print()
print()

print("TRAN    TRAN        TRAN              PAYMENT   AMOUNT      HST         TOTAL")
print("ID      DATE        DETAILS           METHOD")
print("=================================================================================")
print()

# Initialize counters and accumulators for summary / analytics.

TotalRevAcc = 0

# Open the file with the "r" mode for read.
f = open("Revenue.dat", "r")


# Set up the loop to process all the records in the file.
for RevenueRecord in f:      
    # Input - read the first record and split into a list.
    RevenueLst = RevenueRecord.split(",")
   
   
    #Assign variables to each item in the list that are required in the report.
    # The .strip() method removes any spaces in the front or back of a value.
    TranID = RevenueLst[0].strip()
    TranDate =RevenueLst[2].strip()
    TranDetails =RevenueLst[3].strip()
    '''PayMethod = "CASH"''' 
    Amount = float(RevenueLst[4].strip())
    HST = float(RevenueLst[5].strip())
    Total = float(RevenueLst[6].strip())
    
    
    
    
    print(f"{TranID:<3s}     {TranDate:<10s}  {TranDetails:<12s}           {FV.formatMoney(Amount):>9s}  {FV.formatMoney(HST):>9s} {FV.formatMoney(Total):>12s}")
    
    # Increment and Accumulate the summary / analytics data
    TotalRevAcc += Total
    
# Close the file.
f.close()
# Print the summary / analytics data.
print("=================================================================================")


print(f"                                                    Total Revenue:    {FV.formatMoney(TotalRevAcc):>9s}")
print()
print()
print()
print()


print("EXPENSES DETAILS:")
print()
print()
print()

print("INVOICE  INVOICE     ITEM      QTY   DESCRIPTION  COST       HST     TOTAL")
print("NUMBER   DATE        NUMBER")
print("=================================================================================")
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
    ItmNum =ExpensesLst[3].strip()
    '''PayMethod = "CASH"''' 
    Qty = ExpensesLst[4].strip()
    ''' Descrp =ExpensesLst[5].strip()'''
    TotalFE = float(ExpensesLst[5].strip())
    
    
    
    
    print(f"{InvNum:<4s}     {InvDate:<10s}  {ItmNum:<3s}        {Qty:>2s}                                {FV.formatMoney(TotalFE):>10s}")
    # Increment and Accumulate the summary / analytics data
    TotalExpAcc += TotalFE
        
# Close the file.
f.close()
# Print the summary / analytics data.
print("============================================================================")

print(f"                                                    Total Expenses:{FV.formatMoney(TotalExpAcc):>9s}")

Balance = TotalRevAcc - TotalExpAcc
print(f"Balance: {FV.formatMoney(Balance):>9s}")

print()