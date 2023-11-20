
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