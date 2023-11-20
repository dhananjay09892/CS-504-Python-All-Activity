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
