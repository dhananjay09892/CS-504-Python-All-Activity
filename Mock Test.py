# Question 1
# Write a function to calculate the sum of all numbers divisible by 5 between 1 and 1000 (a thousand).
# Both numbers are included. Invoke the function to put the result on the screen.
def sumDivisibleBy5(start, end):
    count = 0
    for i in range(start, end + 1):
        if i % 5 == 0:
            count += i
    return count


print(sumDivisibleBy5(1, 1000))

# Question 2
# Write a program to slice out and print the extensions (like ca, net, com) from the following list of e-mail addresses.
# list1 = ['wmszeliga@yahoo.ca', 'osaru@verizon.net', 'wildixon@outlook.com', 'drhyde@gmail.com']

list1 = [
    "wmszeliga@yahoo.ca",
    "osaru@verizon.net",
    "wildixon@outlook.com",
    "drhyde@gmail.com",
]
for item in list1:
    sliceItem = item.split(".")
    print(sliceItem[-1])


# Question 3
# Write a program to create a file (newlist.txt).
# Find all the lines that start with ‘Content-Length:’ in mbox1.txt and put those lines into the newlist.txt file.

file = open("newlist.txt", "w")
portal = open("mbox1.txt")
for line in portal:
    if line.startswith("Content-Length:"):
        file.write(line)


# Question 4
# Write a program to open the file randomtext.txt.
# Create an empty list and put each word from the file into the list if it is not a duplicate.
# When your list is complete, sort it in alphabetical order and print it.


portal = open("randomtext.txt")
newList = []

for line in portal:
    words = line.split()
    for word in words:
        if word not in newList:
            newList.append(word)

newList.sort()
print(newList)
