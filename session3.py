import random

"""" Random """


""""Exercise 3.8: Not Quite Roulette

Ask the user to enter the following three things using input():

The amount they want to bet
A colour (red or black)
A number between 1 and 100
After generating a random number and colour:

If the colour matches, the users keeps the amount that was bet
If the number matches, the users wins double the amount that was bet
If the colour and number matches, the users wins 100 times the amount that was bet
When neither the colour or number matches the user wins 0
Output the amount the user won
The following code will generate a random number and colour: """

def colour():
    random_number = random.randint(1, 2)

    if random_number == 1:
        colour = 'red'
    else:
        colour = 'black'

    return colour


random_number = random.randint(1, 100)
random_colour = colour()
user_bet= input("Place your bet ")
user_colour = input("Choose color red/black ")
user_number = int(input("Choose a number between 1 and 100 "))

if user_colour == random_colour:
    user_bet = user_bet
    print("You have won " + user_bet)
elif user_number == random_number:
    user_bet = user_bet*2
    print("You have won " + user_bet)
elif user_number == random_number and user_colour == random_colour:
    user_bet=user_bet*100
    print("You have won " + user_bet)
else:
    print("You have lost all your money")

"""Exercise 3.7: This program simulates rock, paper, scissors. 
The first winning condition has been added. 
To finish the program you'll need to add all of the other winning and losing conditions."""

def random_choice():
    choice_number = random.randint(1, 3)

    if choice_number == 1:
        choice = 'rock'
    elif choice_number == 2:
        choice = 'scissors'
    else:
        choice = 'paper'
    return choice

my_choice = input('Choose rock, scissors or paper: ')
opponent_choice = random_choice()

print('Your opponent chose {}'.format(opponent_choice))

if my_choice == 'rock' and opponent_choice == 'scissors':
    print('You win!')
if my_choice == 'paper' and opponent_choice == 'rock':
    print('You win!')
if my_choice == 'paper' and opponent_choice == 'scissors':
    print('You lost!')

else:
    print('Lose-lose situation')



"""Exercise 3.6: This program uses random to simulate a coin flip.

To finish the program you will need to add the following:

If the random coin flip matches the choice input by the user then they win
Otherwise if the random coin flip does not match the choice input by the user then they lose"""

guess_coin_flip = input("Head or tails")
random_coin_flip = random.randint(1,2)

if guess_coin_flip ==1:
    side = "heads"
else:
    side = "tails"

if random_coin_flip == guess_coin_flip:
    print("You won")
else:
    print("You have lost")


random_integer = random.randint(1, 100)
print(random_integer)

sides = int(input('How many sides does the die have? '))
random_integer = random.randint(1, sides)
print('You rolled a {}'.format(random_integer))

"""Comparison operators, logical operator, if statements"""
burger_price = input("Enter your money amount ")
is_price_greater10 = int(burger_price) <= 10
vegetarian_option = input("Is it vegetarian? y/n ")
is_vegetarian = vegetarian_option == "y"
order_burger = is_price_greater10 and is_vegetarian
print("The burger is good for you: {}".format(order_burger))

"""Logical operators   and, or, not """
"""If statement condition, semicolon, body"""
name = input("What is your name? ")
is_admin = name == 'admin'

password = input("What is your password? ")
is_password_correct = password == 'dinosaurs'

if is_admin and is_password_correct:
    print('Welcome')

if not is_admin or not is_password_correct:
    print('Go away')

burger_price = input("Enter your money amount ")
is_price_greater10 = int(burger_price) <= 10
vegetarian_option = input("Is it vegetarian? y/n ")
is_vegetarian = vegetarian_option == "y"
if is_price_greater10 and is_vegetarian:
    print("The restaurant is good choice")
if not is_price_greater10 or not is_vegetarian:
    print("The restaurant is not a good choice")

"""Else statements"""
burger_price = input("Enter your money amount ")
is_price_greater10 = int(burger_price) <= 10
vegetarian_option = input("Is it vegetarian? y/n ")
is_vegetarian = vegetarian_option == "y"
if is_price_greater10 and is_vegetarian:
    print("The restaurant is good choice")
else:
    print("The restaurant is not a good choice")

meal_price = float(input('How much did the meal cost? '))

discount_choice = input('Do you have a discount? y/n ')

discount_applicable = discount_choice == 'y' and meal_price >= 20
if discount_applicable:
    meal_price = meal_price * 0.9
    print("Discount applied")
else:
    print("No discount")
print("Total cost: {}".format(meal_price))

"""" if - elif 
Exercise 3.5: 
You're cooking a pizza and need to check that the oven is at the right temperature.

Write a program to:

Ask the user to input the temperature
Prints "The oven is too hot" if the temperature is over 200
Prints "The oven is too cold" if the temperature is under 150
Prints "The oven is at the perfect temperature" if the temperature is 180
Prints "The temperature is close enough" for any other temperature """


temperature = int(input("What is the temperature? "))
if temperature >= 200:
    print("The oven is too hot")
elif temperature <= 150:
    print("The oven is too cold" )
elif temperature == 180:
    print("The oven is at the perfect temperature")
else:
    print("The temperature is close enough")


