import random

'''Question 1
I have a list of things I need to buy from my supermarket of choice.
shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]

print(shopping_list[1])
I want to know what the first thing I need to buy is. However, when I run the program it shows me a
different answer to what I was expecting?
What is the mistake? How do I fix it?'''

shopping_list = [
"oranges",
"cat food",
"sponge cake",
"long-grain rice",
"cheese board",
]
print(shopping_list[0])

"""I'm setting up my own market stall to sell chocolates. I need a basic tool to check the prices of
different chocolates that I sell.
I've started the program and included the chocolates and their prices. Finish the program by asking
the user to input an item and then output its price.

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,"""

chocolates = {
'white': 1.50,
'milk': 1.20,
'dark': 1.80,
'vegan': 2.00,
}
chocolate_choice = input("Choose your type of chocolate white, milk, dark, vegan? ")
for chocolate in chocolates:
    if chocolate == chocolate_choice:
        print("Your chosen chocolate price is {} $".format(chocolates[chocolate]))

""" Write a program that simulates a lottery. The program should have a list of seven numbers that
represent a lottery ticket. It should then generate seven random numbers. After comparing the two
sets of numbers, the program should output a prize based on the number of matches:
● £20 for three matching numbers
● £40 for four matching numbers
● £100 for five matching numbers
● £10000 for six matching numbers
● £1000000 for seven matching numbers"""

lottery_ticket = []
ticket_length = 7
for nmb in range(ticket_length):
    lucky_numbers = int(input("Provide number from"))
    lottery_ticket.append(lucky_numbers)
print(lottery_ticket)
winning_ticket = []
for nmb in range(ticket_length):
    nmb = random.randint(1, 7)
    winning_ticket.append(nmb)
print(winning_ticket)
matches = set(lottery_ticket).intersection(set(winning_ticket))

if len(matches) == 3:
    print(" £20 for{}matches".format(matches))
elif len(matches) == 4:
    print(" £40 for{}matches".format(matches))
elif len(matches) == 5:
    print(" £100 for{}matches".format(matches))
elif len(matches) == 6:
    print(" £10000 for{}matches".format(matches))
elif len(matches) == 7:
    print(" £100000 for{}matches".format(matches))
else:
    print("Maybe next time")

