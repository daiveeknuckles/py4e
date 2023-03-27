"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 

Once 'done' is entered, print out the largest and smallest of the numbers.

If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 

Enter 7, 2, bob, 10, and 4 and match the output below.
"""

# Establishes that the largest and smallest number does not exist as of now:
largest = None
smallest = None

while True :
    num = input("Enter a number: ")
    if num == "done" :
        break         # break stops the loop and exits. 

# use the try-except function to catch input error if variable "num" is not a number.
    try:
        inum = int(num)   # Converts the input to an integer
    except:
         print('Invalid input')
         continue    # continue causes loop to start again from the top.
   
    # print(fnum)
    if largest is None or inum > largest:
        largest = inum
    elif smallest is None or inum < smallest:
        smallest = inum
        
print("Maximum is", largest)
print("Minimum is", smallest)

