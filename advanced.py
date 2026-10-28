# # # Abstract Method 
# from abc import ABC, abstractmethod

# # class Vehicle(ABC):

# #     @abstractmethod
# #     def start_engine(self):
# #         pass


# # class Car(Vehicle):
# #     def start_engine(self):
# #         return "Car engine started"

# # class Motorcycle(Vehicle):
# #     pass

# # car = Car()
# # print(car.start_engine())




# from abc import ABC, abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def pay(self, amount):
#         pass

#     def receipt(self, amount):                 # shared behaviour is allowed
#         return f"Paid N{amount:,} by {self.pay(amount)}"

# class Card(Payment):
#     def pay(self, amount):
#         return "card"

# class Transfer(Payment):
#     def pay(self, amount):
#         return "bank transfer"

# print(Card().receipt(5000))
# assert Card().receipt(5000) == "Paid N5,000 by card"
# try:
#     Payment()                                  # not allowed
# except TypeError as e:
#     print("Blocked:", e)
# else:
#     raise AssertionError("abstract class was created")

# class Cash(Payment):                           # forgot to write pay()
#     pass
# try:
#     Cash()
# except TypeError:
#     print("Cash is incomplete")
# else:
#     raise AssertionError("incomplete class was created")


# Make the Week 1 Book an abstract Item with abstract loan_days(). Textbook is 7 days, Novel is 14 days. Add a Library.due_in(title) method that uses it. item, textbook, novel, library classes. Use polymorphism to get the loan_days() of the item.

# Build a Pizza class that has a list of Topping objects. A Topping has a name and price as parameters; Pizza.price() is base price + toppings, making base_price a parameter of pizza class .




# singleton pattern: one instance of a class is created and shared across the application. It is used when you want to ensure that there is only one instance of a class and provide a global point of access to that instance.
class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
assert Config() is Config()


# factory pattern: a factory class is used to create objects of different classes based on some input. It is used when you want to create objects without specifying the exact class of object that will be created.

class Dog:
    def speak(self):
        return "Woof"
class Cat:
    def speak(self):
        return "Meow"

def animal_factory(animal_type):
    if animal_type == "dog":
        return Dog()
    elif animal_type == "cat":
        return Cat()
    else:
        raise ValueError("Invalid animal type")

assert animal_factory("dog").speak() == "Woof"


# observer pattern: a subject maintains a list of observers and notifies them of any state changes. It is used when you want to decouple the subject from its observers and allow them to communicate without knowing about each other.

class Shop:
    def __init__(self):
        self._subscribers = []
    def subscribe(self, callback):
        self._subscribers.append(callback)
    def restock(self, item):
        for notify in self._subscribers:
            notify(item)

inbox = []
shop = Shop()
shop.subscribe(lambda item: inbox.append(f"Ada: {item} is back"))
shop.subscribe(lambda item: inbox.append(f"Tunde: {item} is back"))
shop.restock("Rice")
assert inbox == ["Ada: Rice is back", "Tunde: Rice is back"]