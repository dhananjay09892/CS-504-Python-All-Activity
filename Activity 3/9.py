# 9.	Write a program for a company that sells peppermint bark in bulk. The price is $10 for a container. The company has a discount policy of 10% for orders of more than 50 containers and 20% for more than 100. 

# •	Ask the user to enter the number of containers purchased.
# •	Display with a message, the discount amount, and the total price according to the quantity of purchase.

# ‘Your total is 100 dollars today. You had a discount of 20 dollars.’

try:
    containers = int(input("Enter the number of containers purchased: "))
    if containers > 0:
        if containers <= 50:
            discount = 0
        elif containers <= 100:
            discount = 0.10
        else:
            discount = 0.20
        price = containers * 10
        discount_amount = price * discount
        total = price - discount_amount
        print("Your total is $" + str(total) + " today. You had a discount of $" + str(discount_amount) + ".")
    else:
        print("Error: Not a positive number")
except:
    print("Error: Not a number")