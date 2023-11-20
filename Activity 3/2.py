# 2.	Write a program that asks the user for a positive number input.

# •	Check if the input is a positive number and if so,
# o	Check if the number is smaller than 10, 100 and 1000 respectively and print the number of digits the number has. (Single Digit, Double Digits, etc.)
# o	If the number is greater than 1000, print ‘Lots of Digits’.
# •	If the input is not a positive number, print an error message accordingly.
# •	Put your code in a try/except block and print an error message if the user fails to enter a valid number.
try:
    positive_number = int(input("Enter a positive number: "))
    if positive_number > 0:
        if positive_number < 10:
            print("Single Digit")
        elif positive_number < 100:
            print("Double Digits")
        elif positive_number < 1000:
            print("Triple Digits")
        else:
            print("Lots of Digits")
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")
