# 3.	Write a program to print ‘Good Job’ if the user input is a multiple of 8 and ‘Try Again’ if not.  
try:
    user_input = int(input("Enter a number: "))
    if user_input % 8 == 0:
        print("Good Job")
    else:
        print("Try Again")
except:
    print("Error: Not a number")