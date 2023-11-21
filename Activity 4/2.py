
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
