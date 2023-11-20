# 6.	Write a mini-calculator program that asks the user for two numbers and one of four mathematical operators (+,-, *, /) to print out the result with a message. 
# If the user fails to enter one of the four operators, print out an error message.

# Ex: First Number: 5			First Number: 5
#     Second Number: 7        Second Number: 7
# 	Operation: *			Operation: division
# 	Result: 35				Please Enter a Valid Operator!
try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    operator = input("Enter an operator (+,-,*,/): ")
    if operator == "+":
        print(str(first_number) + " + " + str(second_number) + " = " + str(first_number + second_number))
    elif operator == "-":
        print(str(first_number) + " - " + str(second_number) + " = " + str(first_number - second_number))
    elif operator == "*":
        print(str(first_number) + " * " + str(second_number) + " = " + str(first_number * second_number))
    elif operator == "/":
        print(str(first_number) + " / " + str(second_number) + " = " + str(first_number / second_number))
    else:
        print("Please Enter a Valid Operator!")
except:
    print("Error: Not a number")