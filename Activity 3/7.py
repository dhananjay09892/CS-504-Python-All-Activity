# 7.	Write a program for the HR department to calculate wages for prospective employees.

# •	Ask the user for inputs of age, education level and years of experience of the employee.
#     o	Make the user select one of the three education levels; Bachelor, Master’s or PhD by typing either B, M or P as the input.
# •	Calculate the wage according to the following criteria.
#     o	Between the ages 18 and 30, the wages are $1000 per week.
#     o	Between the ages 31 and 60, the wages are $1200 per week.
#     o	The wages increase per level of education; +10% for Bachelors, +20% for Master’s and +30% for PhD degrees.
#     o	Over 10 years of experience is another %10 increase.
# •	Print out the wages with a message. 

try:
    age = int(input("Enter your age: "))
    education_level = input("Enter your education level (B, M or P): ")
    years_of_experience = int(input("Enter your years of experience: "))
    if age > 0 and years_of_experience > 0:
        if age >= 18 and age <= 30:
            wage = 1000
        elif age >= 31 and age <= 60:
            wage = 1200
        else:
            print("Error: Not a valid age")
        if education_level == "B":
            education_extra = wage * 0.10
        elif education_level == "M":
            education_extra = wage * 0.20
        elif education_level == "P":
            education_extra = wage * 0.30
        else:
            education_extra = 0
            print("Error: Not a valid education level")
        if years_of_experience > 10:
            experience_extra = wage * 0.10
        else:
            experience_extra = 0
        wage = wage + education_extra + experience_extra
        print("Your wage is $" + str(wage))
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")