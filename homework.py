animal = input("Do you like dogs or cats more?")
pet_name = input("What would you name your pet?")
print("You like {} and you would name your pet {}".format(animal, pet_name))


def pizza(friends):
    pizzas = float(friends) * 0.5
    return pizzas


friends = input("How many friends you are having for party?")
print("You need {} pizzas for {} friends".format(pizza(friends), friends))
