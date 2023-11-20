# 4.	Write a program to calculate the total amount the user needs to pay for some oranges and bananas.

# •	Decide on the price of each of these items.
# •	Ask the user how many of each item he/she bought.
# •	Calculate the final amount they need to pay and print it with a message.

# The total amount you need to pay is 48 dollars.

price_oranges = 2
price_bananas = 1
oranges = int(input("How many oranges did you buy? "))
bananas = int(input("How many bananas did you buy? "))
total = price_oranges * oranges + price_bananas * bananas
print("The total amount you need to pay is", total, "dollars.")
