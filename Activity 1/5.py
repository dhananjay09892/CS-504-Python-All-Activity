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

