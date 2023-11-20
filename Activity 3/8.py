# 8.	Write a program that calculates a person’s body mass index (BMI). A person’s BMI is calculated with the formula below where weight is measured in pounds and height is measured in inches.

# BMI = 703 * weight / height²

# •	Ask the user to enter his or her weight and height, then print the user’s BMI with a message. 
# •	Also print out a message indicating whether the person has optimal weight, is under optimal weight, or is over optimal weight according to the following criteria.
#     o	A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25.
#     o	If the BMI is less than 18.5, the person is considered to be under optimal weight.
#     o	If the BMI value is greater than 25, the person is considered to be over optimal weight.

try:
    weight = int(input("Enter your weight in pounds: "))
    height = int(input("Enter your height in inches: "))
    if weight > 0 and height > 0:
        bmi = 703 * weight / height**2
        print("Your BMI is " + str(bmi))
        if bmi < 18.5:
            print("You are under optimal weight")
        elif bmi > 25:
            print("You are over optimal weight")
        else:
            print("You are at optimal weight")
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")