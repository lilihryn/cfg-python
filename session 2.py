# age = input("What is your age?")
# print(type(age))
# print("Hello, I am {} yo".format(age))
for number in range(5):
    print(number)
for character in 'Banana':
    print(character)
for character in 'Banana':
    print('<' + character + '>')
for name in ['Mary', 'Ranjit', 'Fatima']:
    print(name)

store_capacity = 5

while store_capacity > 0:
    print('Please come in. Spaces available: ' + str(store_capacity))
    store_capacity = store_capacity - 1

print("\nPlease wait for someone to exit the store.")


def hello(name):
    print('Hello,', name)


hello('Maria')
hello('Kim')
hello('Olya')


def some_function(name, job):
    print(name, 'is a', job)


some_function('developer', 'Fiona')


def some_function(name, job='developer'):
    print(name, 'is a', job)


some_function('Fiona')

some_function('Fiona', 'manager')


def sum_of(x, y):
    return x + y


result = sum_of(10, 15)

print("result is: {}".format(result))


def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area


circle_1 = circle_area(10)
print(circle_1)


def days_in_hours(days):
    hours = days * 24
    return hours


print(days_in_hours(10))