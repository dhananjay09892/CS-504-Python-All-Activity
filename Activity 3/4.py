# 4.	Write a program to calculate the electricity bill.

# •	Ask the user to enter how many kilowatts of electricity they have used that month.
# •	Calculate the bill according to the following criteria.
#     o	The first 100 kilowatts are always free of charge.
#     o	If up to and including 1,000 kws, the price is 10 cents per kw.
#     o	If more than 1.000 kws, the price is 15 cents per kw (first 100 kws are still free).  
# •	Print the bill amount with a message.

# •	Put your code in a try/except block and print an error message if the user fails to enter a valid number.

try: 
    kilowatts = int(input("Enter the number of kilowatts used: "))
    if kilowatts > 0:
        if kilowatts <= 1000:
            if kilowatts <= 100:
                print("Your bill is $0.00")
            else:
                bill = (kilowatts - 100) * 0.10
                print("Your bill is $" + str(bill))
        else:
            bill = (kilowatts - 100) * 0.15
            print("Your bill is $" + str(bill))
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")