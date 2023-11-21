
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