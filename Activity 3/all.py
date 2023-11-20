
# 1.	Please find out if there are line/lines that will never run in the following codes.

number = input('Please Enter a Number: ')
number = int(number)
if number < 100:
    print('Small')
elif number >= 100:
    print('Big')
else:
    print('Neither Small nor Big')

# Solution: Yes, else statement will never run.
# And


number = input('Please Enter a Number: ')
number = int(number)
if number < 100:
    print('Small')
elif number < 80:
    print('Smaller')
elif number < 50:
    print('Even Smaller')
else:
    print('An interesting number') 

# Solution: Yes, 2nd and 3rd if statements will never run.

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


# 3.	Write a program to print ‘Good Job’ if the user input is a multiple of 8 and ‘Try Again’ if not.  
try:
    user_input = int(input("Enter a number: "))
    if user_input % 8 == 0:
        print("Good Job")
    else:
        print("Try Again")
except:
    print("Error: Not a number")

# 4.	Write a program to calculate the electricity bill.

# •	Ask the user to enter how many kilowatts of electricity they have used that month.
# •	Calculate the bill according to the following criteria.
#     o	The first 100 kilowatts are always free of charge.
#     o	If up to and including 1,000 kws, the price is 10 cents per kw.
#     o	If more than 1.000 kws, the price is 15 cents per kw (first 100 kws are still free).  
# •	Print the bill amount with a message.

# •	Put your code in a try/except block and print an error message if the user fails to enter a valid number.

try: 
    kilowatts = int(input("Enter the number of kilowatts used: "))
    if kilowatts > 0:
        if kilowatts <= 1000:
            if kilowatts <= 100:
                print("Your bill is $0.00")
            else:
                bill = (kilowatts - 100) * 0.10
                print("Your bill is $" + str(bill))
        else:
            bill = (kilowatts - 100) * 0.15
            print("Your bill is $" + str(bill))
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")


# 5.	Write a program to calculate the bonus amount of an employee.

# •	Ask user for their yearly salary and years of service.
# •	Calculate the bonus according to the following criteria.
#     o	Up to and including 5 years is 3%
#     o	Between 6 and 10 years is 5% 
#     o	Over 10 years is 10%
# •	Print the bonus amount with a message.
# •	Put your code in a try/except block and print an error message if the user fails to enter a valid number.

try:
    salary = int(input("Enter your yearly salary: "))
    years_of_service = int(input("Enter your years of service: "))
    if salary > 0 and years_of_service > 0:
        if years_of_service <= 5:
            bonus = salary * 0.03
            print("Your bonus is $" + str(bonus))
        elif years_of_service <= 10:
            bonus = salary * 0.05
            print("Your bonus is $" + str(bonus))
        else:
            bonus = salary * 0.10
            print("Your bonus is $" + str(bonus))
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")

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


# 7.	Write a program for the HR department to calculate wages for prospective employees.

# •	Ask the user for inputs of age, education level and years of experience of the employee.
#     o	Make the user select one of the three education levels; Bachelor, Master’s or PhD by typing either B, M or P as the input.
# •	Calculate the wage according to the following criteria.
#     o	Between the ages 18 and 30, the wages are $1000 per week.
#     o	Between the ages 31 and 60, the wages are $1200 per week.
#     o	The wages increase per level of education; +10% for Bachelors, +20% for Master’s and +30% for PhD degrees.
#     o	Over 10 years of experience is another %10 increase.
# •	Print out the wages with a message. 

try:
    age = int(input("Enter your age: "))
    education_level = input("Enter your education level (B, M or P): ")
    years_of_experience = int(input("Enter your years of experience: "))
    if age > 0 and years_of_experience > 0:
        if age >= 18 and age <= 30:
            wage = 1000
        elif age >= 31 and age <= 60:
            wage = 1200
        else:
            print("Error: Not a valid age")
        if education_level == "B":
            education_extra = wage * 0.10
        elif education_level == "M":
            education_extra = wage * 0.20
        elif education_level == "P":
            education_extra = wage * 0.30
        else:
            education_extra = 0
            print("Error: Not a valid education level")
        if years_of_experience > 10:
            experience_extra = wage * 0.10
        else:
            experience_extra = 0
        wage = wage + education_extra + experience_extra
        print("Your wage is $" + str(wage))
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")


# 8.	Write a program that calculates a person’s body mass index (BMI). A person’s BMI is calculated with the formula below where weight is measured in pounds and height is measured in inches.

# BMI = 703 * weight / height²

# •	Ask the user to enter his or her weight and height, then print the user’s BMI with a message. 
# •	Also print out a message indicating whether the person has optimal weight, is under optimal weight, or is over optimal weight according to the following criteria.
#     o	A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25.
#     o	If the BMI is less than 18.5, the person is considered to be under optimal weight.
#     o	If the BMI value is greater than 25, the person is considered to be over optimal weight.

try:
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    if weight > 0 and height > 0:
        bmi = 703 * weight / height**2
        print("Your BMI is " + str(bmi))
        if bmi < 18.5:
            print("You are under optimal weight")
        elif bmi > 25:
            print("You are over optimal weight")
        else:
            print("You are at optimal weight")
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")


# 9.	Write a program for a company that sells peppermint bark in bulk. The price is $10 for a container. The company has a discount policy of 10% for orders of more than 50 containers and 20% for more than 100. 

# •	Ask the user to enter the number of containers purchased.
# •	Display with a message, the discount amount, and the total price according to the quantity of purchase.

# ‘Your total is 100 dollars today. You had a discount of 20 dollars.’

try:
    containers = int(input("Enter the number of containers purchased: "))
    if containers > 0:
        if containers <= 50:
            discount = 0
        elif containers <= 100:
            discount = 0.10
        else:
            discount = 0.20
        price = containers * 10
        discount_amount = price * discount
        total = price - discount_amount
        print("Your total is $" + str(total) + " today. You had a discount of $" + str(discount_amount) + ".")
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")