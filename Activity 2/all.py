# 1.	Follow the steps of the pseudo code to create a program on Python.

# •	Create a variable, number1, and give it a value of 8.
# •	Create another variable, number2, and give it a value of 12.
# •	Add the two variables to create a third variable, number3.
# •	Add 6 to number 1 and 8 to number2.
# •	Multiply number1 and number2 and store the value in number3.
# •	Print each of the 3 variables with a message.

# Ex: ‘The value for number1 is 54’

number1 = 8
print("The value for Number1 is ",number1)
number2 = 12
print("The value for Number2 is ",number2)
number3 = number1 + number2
print("The value for Number3 is ",number3)
number1 += 6
print("The value for Number1 is ",number1)
number2 += 8
print("The value for Number2 is ",number2)
number3 = number1 * number2
print("The value for Number3 is ",number3)

# 2.	Write a program to find the average grade of four subjects; geography, history, math and science.

# •	Ask the user to enter the marks for each of the courses. 
# •	Calculate the average grade.
# •	Print out the result with a message.

# Note: The grade scale is 0-100.

# Sample Output:
# Enter your geography marks: 90
# Enter your history marks: 80
# Enter your math marks: 70
# Enter your science marks: 60
# Your average grade is 75.0

# Solution:
# Input marks
geography = float(input("Enter your geography marks: "))
history = float(input("Enter your history marks: "))
math = float(input("Enter your math marks: "))
science = float(input("Enter your science marks: "))
# Calculate average
average = (geography + history + math + science) / 4
# Display result
print("Your average grade is", average)


# 3.	Write a program to accept radius of circle and display its area and circumference.

# •	Create a PInumber variable and give it a value of 3.
# •	Ask the user for the radius of the circle.
# •	Print out the circumference and the area of the circle with a message.

# “The circumference of the circle is … and its area is ….”

# Circumference of a circle = 2πr
# Area of circle = πr²


PInumber = 3
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * PInumber * radius
area = PInumber * radius * radius
print("The circumference of the circle is", circumference, "and its area is", area)


# 4.	Write a program to calculate the total amount the user needs to pay for some oranges and bananas.

# •	Decide on the price of each of these items.
# •	Ask the user how many of each item he/she bought.
# •	Calculate the final amount they need to pay and print it with a message.

# The total amount you need to pay is 48 dollars.

price_oranges = 2
price_bananas = 1
oranges = int(input("How many oranges did you buy? "))
bananas = int(input("How many bananas did you buy? "))
total = price_oranges * oranges + price_bananas * bananas
print("The total amount you need to pay is", total, "dollars.")


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


# 6.	Write a program to calculate the check at a restaurant. 

# •	The items on the menu have the following prices; 
    # o	Individual pizzas $10
    # o	Soft drinks $2
    # o	Desserts $5. 
# •	Calculate the check for a party of 3 who had 1 of each item.
# •	Calculate the tax amount to be added to the bill (7 percent sales tax).
# •	Calculate the tip (18 percent).
# •	Calculate the total bill and display all the information in the following format.

# HINT: You can use the round function to round up the tax and tip if necessary. You can also limit the number of decimal points to two.

# o	round(tax, 2)



# Meal: $.....
# Tax: $.....
# Tip: $.....
# Total Bill: $.....
price_pizza = 10
price_drink = 2
price_dessert = 5
pizza = 1
drink = 1
dessert = 1
meal = price_pizza * pizza + price_drink * drink + price_dessert * dessert
tax = meal * 0.07
tip = meal * 0.18
total = meal + tax + tip
print("Meal: $", meal)
print("Tax: $", round(tax, 2))
print("Tip: $", tip)
print("Total Bill: $", total)

