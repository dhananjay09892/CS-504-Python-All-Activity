

# 4.	Write a program to calculate your Christmas road trip cost and print the output. 

# •	Get user input for the number of nights, the flight destination, and total days for the rental car. 
# •	Create 3 functions to calculate hotel cost, flight cost, and rental car cost. Use return statements in your functions. 
#     o	For the hotel price function, use $150 per night (return the result)
#     o	Include 4 destinations for the flight and different prices for each (ex. $150 for Raleigh, $200 for Miami, $250 for Austin, $400 for San Diego)
#     o	Calculate the car rental price (ex. use $50 per day) 
#         	Make a discount of $50 if the rental period is 7 days or more.
#         	Make a discount of $30 if the rental period is 3 days or more.
#         	Customers cannot get both discounts.
# •	Create 4 print functions with the total price of hotel, flight, rental and the grand total.

def hotel(nights):
    return nights * 150
def flight(dest):
    if dest == 'Raleigh':
        return 150
    elif dest == 'Miami':
        return 200
    elif dest == 'Austin':
        return 250
    elif dest == 'San Diego':
        return 400
    else:
        return 'Invalid destination'
def rental(days):
    if days >= 7:
        return (days * 50) - 50
    elif days >= 3:
        return (days * 50) - 30
    else:
        return days * 50
def print_hotel(nights):
    print('Hotel cost: $', hotel(nights), sep='')
def print_flight(dest):
    print('Flight cost: $', flight(dest), sep='')
def print_rental(days):
    print('Rental cost: $', rental(days), sep='')
def print_total(nights, dest, days):
    print('Total cost: $', hotel(nights) + flight(dest) + rental(days), sep='')
nights = int(input('Enter number of nights: '))
dest = input('Enter destination: ')
days = int(input('Enter number of days for rental car: '))
print_hotel(nights)
print_flight(dest)
print_rental(days)
print_total(nights, dest, days)
