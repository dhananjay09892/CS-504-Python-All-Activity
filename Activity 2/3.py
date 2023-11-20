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
