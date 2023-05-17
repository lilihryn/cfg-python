import random

"""lists and dictionaries
List is a collection of values
lottery_numbers= [4,8,15,16]
person=[Jess, 32]
List values can be accessed by index of the value starting from 0
student_names=['Diedre', 'Hank', 'Maram']
print(student_names[0])--> Diedre
Changing the value of element of the list by index
student_names[1]='Joshua'
print(student_names)
"""

clothes = ["shorts", "shoes", "t-shirt"]
if clothes[0] == "shorts":
    clothes[0] = "warm coat"
    print(clothes)
else:
    print(clothes)

"""List functions
len(): the number of items in the list
max(): the biggest value of the list
min(): the smallest value in the list

costs = [1.2, 4.3, 2.0, 0.5]
print(len(costs))
print(max(costs))
print(min(costs)) 

sorted(): sorts the list items in ascendant
reversed(): reverses the order of the list

print(sorted(costs))
print(list(reversed(costs)))
"""
game_scores = [3, 5, 200, 100, 150, 50, 6, 10, 56, 45]
print("Number of scores: {}".format(len(game_scores)))
print("Highest score: {}". format(max(game_scores)))
print("Lowest score: {}". format(min(game_scores)))
print(list(reversed(game_scores)))

""" in operator--checks if the value is in the list(true/false)

student_name = input('Which student are you looking for? ')

students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]

if student_name in students:
    print('{} is in the class'.format(student_name))
else:
    print('{} is not in the class'.format(student_name))

the .append() method is used to add items to the list
students = [
    'Diedre', 'Hank', 'Helena', 'Salome',
]
student_name = input('What is the name of new student? ')
students.append(student_name)
print(students)
"""
shopping_list = ['bread', 'milk', 'coffee']
item = 'butter'
if 'bread' in shopping_list:
    shopping_list.append(item)
    print(shopping_list)
else:
    print(shopping_list)

""" fridge = ["cheese, pizza, coke"]
    if "milk" not in fridge:
    print("You have no milk in the fridge!")
"""

"""Using lists and for loops together
student_names = ['Diedre', 'Hank', 'Helena', 'Salome']
for name in student_names:
    print(name) 
    

"""
costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for spend in costs:
    total_cost = total_cost + spend
print('{:.2f}'.format(total_cost))


total = sum(costs)
print(total)


rand_list = []
for i in range(0, 5):
  num = random.randint(1, 30)
  rand_list.append(num)
print(rand_list)

"""Dictionaries 
Stores a collection of labelled items. Each item has a key and a value
person = {
    'name': 'Jessica',
    'age' : 23,
    'height' : 172
    }
    values in dictionary are accessed using their keys
    print(person['age'])
"""
place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number': '54',
    'location': {
        'longitude': 127,
        'latitude': 63,
    }
}
print(place['name'], place['post_code'],
      place['street_number'])
print(place['location']['longitude'], place['location']['latitude'])

"""Putting dictionaries inside a list 
people = [
    {'name': 'Jessica', 'age': 23},
    {'name': 'Trisha', 'age': 24},
]

for person in people:
    print(person['name'])
    print(person['age']) 

"""
fruits = [
    {'name': 'apple', 'colour': 'red', 'price': 0.12},
    {'name': 'banana', 'colour': 'yellow', 'price': 0.2},
    {'name': 'pear', 'colour': 'green', 'price': 0.19},
]
for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])
"""Random choices
the choice() function in the random module returns a random item from a list
import random
colours = ['red', 'green', 'blue']
chosen_colour = random.choice(colours)
print(chosen_colour)
"""
list_first_names = ['Olga', 'Will', 'Nicolas']
list_last_names = ['Cage', 'Smith', 'Peterson']
random_name = random.choice(list_first_names)+''+random.choice(list_last_names)
print(random_name)
verbs = ['going', 'speaking', 'listening to']
nouns = [' home', ' bananas', ' music']
sentence = random.choice(verbs) + random.choice(nouns)
print(sentence)
