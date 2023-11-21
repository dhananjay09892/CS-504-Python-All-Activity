# 1. Write a program to calculate the sum of all odd numbers between 10 and 100 (use range function) 

# Note: range() function in Python has the following syntax; range(start, stop, step). 
# 	If you need the numbers from 0 to another number, you just specify the ending point(not included), so range(6) gives you 0,1,2,3,4,5. 
# 	If you need a series of numbers within a range, you specify the starting and the ending point(not included), so range(2,6) gives you 2,3,4,5. 
# 	If you need the numbers within a range to increment according to a pattern instead of one-by-one, you specify the increment, so range(2,16,3) gives you 2,5,8,11,14. 
# 	You can use a for loop to go through each number and print them. 

# Ex: 	for i in range(2,16,3) : 
#      	    print(i) 

# 	Create a variable to show the sum of the numbers. 
# 	Construct a loop that iterates through all the numbers in the specified range. 
# 	Check the condition for each number inside the loop. 
# 	Add up the numbers. 
sum = 0
for i in range(11,100,2):
    sum += i
    print(i)


