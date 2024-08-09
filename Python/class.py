# #OOP: Object Oriented Programming

# #CONCEPTS OF OOP
# #CLASS: A blueprint for creating objects. 
# #OBJECT: A particular instance of a class.
# #INHERITANCE: MECHANISM WHERE A NEW CLASS CAN INHERIT ATTRIBUTES AND METHODS FROM AN EXISTING CLASS, BASE OR PARENT CLASS.
# #POLYMORPHISM: Allows object of different classes to be treated as objects of a common superclass


# class Car:
#     def __init__(self, make, model): # Class (blue print), defining attributes make and model
#         self.make = make
#         self.model = model

#     def drive(self): # method (function) drive behaviour
#         print(f'Driving the {self.make} {self.model}')
    
#     def sound(self):
#         print(f'The {self.make} {self.model} makes a vroom sound')

# # TO INHERIT A CLASS AND CREATE OUR OWN CLASS, WE USE THE FOLLOWING SYNTAX

# class ElectricCar(Car): # Creating electricCar(child class) inheriting the behaviuor of our car(parent class) above
#     def charge(self): 
#         print('Charging the {self.make} {self.model}') #Inherits the attributes

# tesla = ElectricCar('Tesla', 'model S') #Creating a copy of ElectricCar. It inherits the behavious of base and subbase classes above.

# # tesla.charge() 
# # tesla.drive()
# # tesla.sound()



# #Polymorphism
# class Animal: # Blue print to demonstrate polymorphism
#     def make_sound(self): # Came with no default, just make sound behavious. Allows us to customise the attributes to suite our need.
#         pass #Means don't return anything, just pass.

# class Dog(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def make_sound(self):
#         print('woof') # The default from the parent class is pass, but we want print('woof) in here. Once we specify it as shown, it ignores the default. That is polymorphism

#     def make_sound(self):
#         print('A dog makes a woof sound') # This will override the parent attribute.
    
# # dog = Dog() # To run the instance of a dog

# # dog.make_sound() # if we run this we would get woof and not just the pass

# class Cat(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def legs(self): # Created my own animal but inherited from the base class(Inheritance)
#         print('A cat has fore legs')
    
#     def make_sound(self):
#         print("A cat makes a meew sound") # This overrides the defaulf (polymophism)

# # cat = Cat()
# # cat.makesound()

# class Cow(Animal): # Show the concept of polymorphism as we override the attribute from the parent class to create what we need
#     def legs(self): # Created my own animal but inherited from the base class(Inheritance)
#         print('A caw has fore legs')
    
#     def make_sound(self):
#         print("A cow makes a moo sound") 
    






 

# Lexus = Car("Toyota", "Lx470") # Object (Subclass copy of the class) of Car. Inherit the attributes of the class Car (ie make, model)
# BMW = Car("BMW", "X6")       # Object (Subclass) of Car. Inherit the attributes of the class Car (ie make, model)




# Lexus.drive() # Calling the behaviour of the blueprint drive behaviour
# BMW.drive() #Calling the behavious of the blueprint

# Goat.sound()
# Cow.sound()

# #WHEN WE HAVE A PROGRAM THAT USERS WILL NEED TO EXTEND AND CREATE THEIR'S, WE CAN USE OOP TO DEFINE A CLASS THAT WILL BE USED TO CREATE OBJECTS THAT WILL INHERIT THE ATTRIBUTES AND BEHAVIOURS OF THE CLASS. THIS WILL HELP US TO AVOID WRITING THE SAME CODE MULTIPLE TIMES.
#REASON FOR OOP: When we have multiple objects that share the same attributes and behaviours, we can use OOP to define a class that will be used to create objects that will inherit the attributes and behaviours of the class. This will help us to avoid writing the same code multiple times.

# import re

# #A valid MasterCard number starts with 51 through 55 and is 16 digits long. 
# def valid_mastercard(number):
#     pattern = r'^(5[1-5][0-9]{14})$'


#     if re.match(pattern, number):
#         print("Valid mastercard number")
#     else:
#         print("Invalid mastercard number")

# mastercard_number = "5391234567891299"



# print(valid_mastercard(mastercard_number))  
# # C

# a = "Hello, World!"
# print(a[12])

# 1, -5, 0, 10 

# a = int('10') #10
# b = 3.14
# b = int(3.14) # 3
# print(b)



# float(2) #2.0


# strings = 'abc1952'
# print(strings[0])


# greeting = "Hello, " + "World!" # Concatenation
# print(greeting)


# print(greeting[12])

# #SLICING
# S = "Hello World!"
# # print(S[7:12]) # orld!
# # print(S[3:5]) # lo
# print(S[:-1]) # Hello World

# print(S[2:-2])
# print(S[-3]) #r

# print(len(S))

# list
# name = ["Alice", "Bob", "Charlie"]

# print(name[0])

# #insert
# name.insert(1 , "Eve")
# print(name)

#Add
# name[1] = "Beatrice"
# print(name)

#Remove
# name.remove('Bob')
# print(name)

# name.pop(0)
# print(name)

# del name[2]
# print(name)

#Tuples

# a = ("apple", "banana", "cherry")
# print(a[0])
# b = list(a)
# b.remove('apple')
# b.pop(2)
# del b[0]
# print(b)

# a = tuple(b)
# print(a)

# for x in range(6):
#      print(x)

#List comprihension

# squares of numbers from 1 to 10

# squares = [x**2 for x in range(0,10)]
# print(squares)


# string = "Hello World"

# upper_case = [x.upper() for x in string]
# print(upper_case)

# a = [x for x in range(6)]
# print(a)

persons = {
     "name": "John",
     "age": 30,
     "city": "New York"
 }

# print(person["city"]) 

# person["age"] = 31

# print(person)

# print(person['name'])
# print(person['sex'])

# print(person.get('sex'))

# print(person.get('sex', 'not provided'))

# print(person.get('Country', 'Country not on the List '))

for key,value in persons.items():
    print(f"{key}:{value}")
    # print(value)
    # print(f"key: {'name'}")


     






# persons = [
#     {"name": "John", "age": 30, "city": "New York"},
#     {"name": "Mark", "age": 50, "city": "PH"}
# ]

#  To change John's age to 31
# for y in persons:
#     if y["name"] == "John":
#         y["age"] = 31


# print(persons)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

aliens = []
for alien_number in range(30): #Returns series of numbers which just tells python how many times we want the loop to repeat
   new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
   aliens.append(new_alien) #We append each new alien to the empty list
#To show the 1st 5 aliens out of the 30 created with slicing
for alien in aliens[:5]:
    print(alien)







