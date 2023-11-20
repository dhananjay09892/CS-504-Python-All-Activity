# 5.	Write a program to calculate the monthly pay of an employee. Get the input for the following and print out the monthly salary with a message.  

# •	How many hours the employee works a day.
# •	How many days the employee works in a week.
# •	Create a rate variable and give it a value of 20 dollars.

# Your monthly salary is 1500 dollars.

hours = int(input("How many hours do you work a day? "))
days = int(input("How many days do you work in a week? "))
rate = 20
monthly_salary = hours * days * rate
print("Your monthly salary is", monthly_salary, "dollars.")
