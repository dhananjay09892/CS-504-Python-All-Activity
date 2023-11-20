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