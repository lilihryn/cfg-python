import csv

"How do I output the species values for each of the dictionaries?"
animals = [
    {'species': 'zebra', 'name': 'Penelope'},
    {'species': 'penguin', 'name': 'Jenn'},
    {'species': 'elephant', 'name': 'Harris'},
    {'species': 'flamingo', 'name': 'Florence'},
]
for animal in animals:
    print(animal['species'])

"Files, pip package manager,APIs"

""""reading, writing files"
with statement, write() 'w'to write '+'to read '\n' new line caracter

with open('people.txt', 'w+') as text_file:
people = 'Joanne \nSusan \nAmina'

    text_file.write(people) 
    
 with open('people.txt', 'r') as text_file:
    contents = text_file.read()

print(contents)   
    
    
 
Exercise 5.1: Create a to-do list program that writes user input to a file

The program should:

Ask the user to input a new to-do item
Read the contents of the existing to-do items
Add the new to do item to the existing to-do items
Save the updated to-do items """


new_item = input('Enter a to-do item: ')

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()

todo = todo + new_item + ' \n'

with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)


new_to_do = input("Enter new item for todo")

with open('todo.txt', 'r') as todo_file:
    todo = todo_file.read()
if new_to_do not in todo:
    todo = todo + '\n' + new_to_do + '\n'
else:
    print("already present")
with open('todo.txt', 'w+') as todo_file:
    todo_file.write(todo)

    """Working with csv file
    writing with DictWriter"""


    field_names = ['name', 'age']

    data = [
        {'name': 'Jill', 'age': 32},
        {'name': 'Sara', 'age': 28},
    ]

    with open('team.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

        spreadsheet.writeheader()
        spreadsheet.writerows(data)

"""Reading a csv 'DictReader'"""
with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))


"""Exercise 5.2: This program is supposed to read data about trees from a file to find the shortest tree. 
Complete the program adding code to open trees.csv.
The trees.csv file included with your student guides. Save the csv file in the same folder as your Python program. """
with open('trees.csv', 'r') as csv_file:
   spreadsheet = csv.DictReader(csv_file)

   heights = []


   for row in spreadsheet:
      tree_height = row['height']
      heights.append(tree_height)

      shortest_height = min(heights)
print(shortest_height)

"""Python pip used via terminal command"""
"""API"""