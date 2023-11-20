# 1.	Write a statement that displays ‘Python is my favorite programming language
print('Python is my favorite programming language')

# 2.	Write a statement that displays:

# Most people think that Jordan is the “G.O.A.T.”

print('Most people think that Jordan is the "G.O.A.T."')
# OR 
print("Most people think that Jordan is the \"G.O.A.T.\"")

# 3.	Write a program to display the following information.
# Name                                          
# Address
# City, State Zip Code
# skip one line here
# Email address
# skip one line here
# Major
# skip one line
# Phone Number

print("John Doe")
print("221 Danbury Road")
print("Wilton, CT 06897")
print("")
print("johndoe@gmail.com\n")
print("Literature",end="\n\n")
print("617 426-9018")


# 4.	Write a program to create 3 variables (x,y,z) with different numbers as values. 
# Write a program to check which one is the biggest number and print out the result with a message. (conditional statements, and keyword)

x = 25
y = 45
z = 55

if x > y and x > z:
    print(f"x({x}) is biggest number.")
elif x < y > z:
    print(f"y({y}) is biggest number.")
else:
    print(f"z({z}) is biggest number.")


# 5.	Write a program to create a variable with a value of 25. 
# Create a loop that prints the square of the variable and changes the value of it by -2 every time it runs. 
# Continue until the variable is not greater than 0 anymore. 
# Print a message to indicate your program has finished (Success!)   

x = 25
for i in range(25,0,-2):
    print(i**2)
print("Success!")

# OR 

while x > 0:
    print(x**2)
    x = x -2
print("Success!")

