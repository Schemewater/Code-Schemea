# File: Payroll.py
# Student: Alec Anaya
# UT EID: aa89468
# Course Name: CS303E
#
# Date: 2/11/2022
# Description of Program: This program asks for input from a user including name, pay rate, hours worked, and amount they are taxed on their earning. The program takes those inputs and outputs a payroll statement.


# Getting user input
print()
name = input("Enter employee's name: ")
hrsWkd = float(input("Enter number of hours worked in a week: "))
hrPay = float(input("Enter hourly pay rate: "))
fed = float(input("Enter federal tax withholding rate: "))
state = float(input("Enter state tax withholding rate: "))
print()

# Making equations for computation 
grossPay = hrsWkd * hrPay
fedWith = fed * grossPay
stateWith = state * grossPay
totalDeduction = fedWith + stateWith
netPay = grossPay - fedWith - stateWith

# Printing the payroll statement
print("Employee name:", name)
print("Hours worked:", format(hrsWkd,".1f"))
print("Gross pay: $" + format(grossPay, ".2f"))
print("Deductions:")
print("    Federal Withholding (" + format(fed, ".1%") + "): $" + format(fedWith, ".2f"))  
print("    State Withholding (" + format(state, ".1%") + "): $" + format(stateWith, ".2f"))
print("    Total Deduction: $" + format(totalDeduction, ".2f"))
print("Net Pay: $" + format(netPay, ".2f"))



