
"""
Assignment 2.3: Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 

Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 

You should use input to read a string and float() to convert the string to a number. 

Do not worry about error checking or bad user data.
"""


# **** SOLUTION: OPTION #1 ****
# To obtain required data, use the input() function:
hrs = input('Enter hours worked: ')
rate = input('Enter rate of pay: ')

# Convert the string data to float:
fhours = float(hrs)
frate = float(rate)

# Compute for the pay:
gross_pay = fhours * frate

# Print final result:
print('Pay:', gross_pay)



# **** SOLUTION: OPTION #2 (Less code!) ******
hours = input("Enter hours worked: ") 
rate = input("Enter rate: ")
gross_pay = float(hours) * float(rate)
print("Pay:", gross_pay)