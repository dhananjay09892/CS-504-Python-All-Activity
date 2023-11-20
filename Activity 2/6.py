# 6.	Write a program to calculate the check at a restaurant. 

# •	The items on the menu have the following prices; 
    # o	Individual pizzas $10
    # o	Soft drinks $2
    # o	Desserts $5. 
# •	Calculate the check for a party of 3 who had 1 of each item.
# •	Calculate the tax amount to be added to the bill (7 percent sales tax).
# •	Calculate the tip (18 percent).
# •	Calculate the total bill and display all the information in the following format.

# HINT: You can use the round function to round up the tax and tip if necessary. You can also limit the number of decimal points to two.

# o	round(tax, 2)



# Meal: $.....
# Tax: $.....
# Tip: $.....
# Total Bill: $.....
price_pizza = 10
price_drink = 2
price_dessert = 5
pizza = 1
drink = 1
dessert = 1
meal = price_pizza * pizza + price_drink * drink + price_dessert * dessert
tax = meal * 0.07
tip = meal * 0.18
total = meal + tax + tip
print("Meal: $", meal)
print("Tax: $", round(tax, 2))
print("Tip: $", tip)
print("Total Bill: $", total)

