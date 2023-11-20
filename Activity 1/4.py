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
