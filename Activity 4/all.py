# 1.	Write a Python function to find the largest of the three numbers entered as the function parameters.

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print(largest(1,2,3))
print(largest(1,3,2))
print(largest(3,2,1))
print(largest(3,1,2))
print(largest(2,1,3))
print(largest(2,3,1))



# 2.	Write a function to convert temperatures from Fahrenheit to Celsius and vice versa.

# •	Ask the user for input in either Fahrenheit or Celsius with a message prompting the user to enter ‘C’ for Celsius or ‘F’ for Fahrenheit first.
# •	Get the source temperature from the user and convert the temperature to the other form using the following formulas.

# C = (F − 32) × 5/9		F = (C × 9/5) + 32

# •	Print out the result with a message.

# ‘The temperature in Fahrenheit is 72 degrees.’

def convert(temp, unit):
    if unit == 'C':
        return (temp * 9/5) + 32
    elif unit == 'F':
        return (temp - 32) * 5/9
    else:
        return 'Invalid unit'
    
unit = input('Enter C for Celsius or F for Fahrenheit: ')
temp = int(input('Enter temperature: '))
print('The temperature in', unit, 'is', convert(temp, unit), 'degrees')



# 3.	Write a function code for a user-made calculator to do 4 basic operations with 2 numbers from the user.

# •	Create 4 functions for 4 basic operations. Each function should have 2 arguments when created.
# •	Create 3 input functions to get the first number, the second number, and the desired type of operation from the user (eg. + for Addition, - for subtraction etc.)
# •	Create 4 conditional statements for each operation and run the appropriate function for that operation.

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return 'Cannot divide by zero'
    else:
        return a/b    
def calc(a,b,op):
    if op == '+':
        return add(a,b)
    elif op == '-':
        return sub(a,b)
    elif op == '*':
        return mul(a,b)
    elif op == '/':
        return div(a,b)
    else:
        return 'Invalid operation'
def get_num():
    return int(input('Enter a number: '))
def get_op():
    return input('Enter an operation: ')
a = get_num()
b = get_num()
op = get_op()
print(calc(a,b,op))




# 4.	Write a program to calculate your Christmas road trip cost and print the output. 

# •	Get user input for the number of nights, the flight destination, and total days for the rental car. 
# •	Create 3 functions to calculate hotel cost, flight cost, and rental car cost. Use return statements in your functions. 
#     o	For the hotel price function, use $150 per night (return the result)
#     o	Include 4 destinations for the flight and different prices for each (ex. $150 for Raleigh, $200 for Miami, $250 for Austin, $400 for San Diego)
#     o	Calculate the car rental price (ex. use $50 per day) 
#         	Make a discount of $50 if the rental period is 7 days or more.
#         	Make a discount of $30 if the rental period is 3 days or more.
#         	Customers cannot get both discounts.
# •	Create 4 print functions with the total price of hotel, flight, rental and the grand total.

def hotel(nights):
    return nights * 150
def flight(dest):
    if dest == 'Raleigh':
        return 150
    elif dest == 'Miami':
        return 200
    elif dest == 'Austin':
        return 250
    elif dest == 'San Diego':
        return 400
    else:
        return 'Invalid destination'
def rental(days):
    if days >= 7:
        return (days * 50) - 50
    elif days >= 3:
        return (days * 50) - 30
    else:
        return days * 50
def print_hotel(nights):
    print('Hotel cost: $', hotel(nights), sep='')
def print_flight(dest):
    print('Flight cost: $', flight(dest), sep='')
def print_rental(days):
    print('Rental cost: $', rental(days), sep='')
def print_total(nights, dest, days):
    print('Total cost: $', hotel(nights) + flight(dest) + rental(days), sep='')
nights = int(input('Enter number of nights: '))
dest = input('Enter destination: ')
days = int(input('Enter number of days for rental car: '))
print_hotel(nights)
print_flight(dest)
print_rental(days)
print_total(nights, dest, days)
