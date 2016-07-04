import random

class Pet(object):

    def __init__(self, name, health = 100, hunger = 20, boredom = 20):

        self.name = name
        self.health = health
        self.hunger = hunger
        self.boredom = boredom
        print(name + " is a beautiful name!")
        

    def return_stats(self):
        print("Name: " + str(self.name))
        print("Health: " + str(self.health))
        print("Hunger: " + str(self.hunger))
        print("Boredom: " + str(self.boredom))
        return self.name, self.health, self.hunger, self.boredom

def next_action():
    
    choice = str(input("Please input \"C\" to continue, "
                   "\n\"S\" to view your pet's stats, "
                    "\n\"P\" to play with your pet, "
                    "\n\"F\" to feed your pet, "
                    "\n\"H\" to take your pet to the vet, and "
                   "\n\"X\" to exit this program. "
                    "\n: "))
    while True:
        
        if choice.upper() in ("C", "S", "P", "F", "H","X"):
            break
        else:
            choice = input("That's not a valid answer. Try again: ")

    return choice


print("Welcome to your virtual pet generator!")
pet_name = str(input("Please name your pet: "))

new_pet = Pet(pet_name)

choice = next_action()
                   
                   
