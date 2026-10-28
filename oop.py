# "OOP"
# OOP (object oriented programming) is a way of writing code where you model things from the real world as objects that carry their own data and their own abilities.

# the two things behind oop is:
# 1. class
#  2. objects
# 3. Atrribute
# 4. Method


# class Dog:
#     pass 

# buddy = Dog()   
# rex = Dog()

# print(type(rex))


# class Dog:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age 

# buddy = Dog("buddy", 3)
# rex = Dog("Bingo", 5)

# # print(buddy.name)
# # print(buddy.age)
# print(rex.name)
# print(rex.age)

# Self simply means "this particular object"


# class Dog:
#     def __init__(self, name, age ):
#         self.name = name
#         self.age = age 

#     def bark(self):
#         print(f"{self.name} says: Woof")

#     def birthday(self):
#         if condition:
#           pass
#         elif condition:
#           pass
#         else:
#           pass
#         self.age += 1
#         print(f"happy birthday {self.name} you are {self.age}")

# buddy = Dog("Bingo", 3)
# buddy.birthday()



# def bark():
#     print("Woof")

# bark()

# inheritance

# animal 
# dog, cat

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(f"{self.name} is eating yam")

# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} is barking")

# class Cat(Animal):
#     def meow(self):
#         print(f"{self.name} says meow")

# mammals = Dog("rex")
# mammals.eat()
# mammals.bark()

# tom =Cat("Tom")
# tom.eat()
# tom.meow()


# polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")

class Cat(Animal):
    # class used
    def speak(self):
        print(f"{self.name} says meow")

class Cow(Animal):
    def speak(self):
        print(f"{self.name} says moo")

class Bird(Animal):
    def speak(self):
        print(f"{self.name} says chirp")

animals = [Dog("bingo"), Cat("Tom"), Cow("Fulani"), Bird("Raven")]

for animal in animals:
    animal.speak()


