# #List is an ordered collection of items
# #List are mutable - Content can be changed
# my_list = [1, 2, 3, 'example', 3.132, [1, 2, 3]] #Square brackets

# #Access items in a list by index - This is done by index
# print(my_list[0])  #1
# print(my_list[5])  # output = [1, 2, 3]

# #List Slicing
# print(my_list[2:5]) # Output = [3, 'example', 3.132] The counting starts 1. So 2 is b/w 2 & 3 and 5 is b/w 3.132 and [1, 2, 3]

# #Modifying list (mutable) - List can be changed by adding or changing: [], .insert(), .append()

# my_list[2] = 'changed' #modified element at index 2 to changed
# print(my_list) #output will be [1, 2, 'changed', 'example', 3.132, [1, 2, 3]]

# my_list.append('added') #To add an element to the list. At the end
# print(my_list) # output will be [1, 2, 'changed', 'example', 3.132, [1, 2, 3], 'added']

# my_list.insert(2, 'inserted') #To insert the string inserted at index 2
# print(my_list) # output will be [1, 2, 'inserted', 'changed', 'example', 3.132, [1, 2, 3], 'added']

#Removing Elements From A List: .pop(), .remove(), del my_list[]
# my_list = [1, 2, 'inserted', 'changed', 'example', 3.132, [1, 2, 3], 'added']

# del my_list[6] #deletes element in index 6
# print(my_list) # output is [1, 2, 'inserted', 'changed', 'example', 3.132, 'added']

# my_list.remove('example') #Removes element by value. here example
# print(my_list) # output here is [1, 2, 'inserted', 'changed', 3.132, 'added']

#Diff between .pop() & .remove(): pop() removes the indexed value while remove() removes the 1st occurence of the item on the list

# my_list.pop(4) #Removes elements by index
# print(my_list) # Output is [1, 2, 'inserted', 'changed', 'added']
# Pop uses indexes but not in [] it's because it's a method and not like indexing used for retrieving elements

# #LIST METHODS:extend(), index(), count(), sort(), reverse(), pop(), insert(),remove(), append()

# index = my_list.index('added') #Finds index of the 1st occurence of the word "added"
# print(index) #output will be 4. Used to find index of items in a list

# count = my_list.count('inserted') #Returns the number of times an item appears in a list
# print(count) # output 1

# my_list = [1, 2, 3, 1, 4, 5, 6, 7, 2, 4, 1]

# my_list.sort() #Sorts all items in ascending or alphabetical format
# print(my_list) # out is [1, 1, 1, 2, 2, 3, 4, 4, 5, 6, 7]

# my_list.reverse() #Reverses the order of items in a list
# print(my_list) # Output is [7, 6, 5, 4, 4, 3, 2, 2, 1, 1, 1]

# my_list.clear() #Clears all items in a list
# print(my_list) # Output is []

# index = my_list.index(4)
# print(index)


#List Comprihension: A concise way to create lists.
#Consist of brackets containing an expression followed by a for statement
#then 0 or more 'for' or 'if' statements.
#syntax: new_list = [expression for item in iterable if condition]

# squares = [x**2 for x in range(10)]
# print(squares) #output: [1,4,9,16,25,36,49,64,81]

#Create a list of uppercase characters from a string
# string = "Helo World"
# uppercase_chars = [x.upper() for x in string] 
# print(uppercase_chars) output: ['H', 'E', 'L', 'O', ' ', 'W', 'O', 'R', 'L', 'D']

# #List of numbers from 1 to 100 divisible by 7
# list = [num for num in range(1, 101) if num%7 == 0] # % is modulus
# print(list) # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]

# #List of words len > 5
# words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# over_fives = [word for word in words if len(word) > 5]
# print(over_fives) #output= ['banana', 'cherry', 'elderberry']

# #List of Numbers with square roots of the numbers that are perfect squares
# numbers = [1, 2, 3, 4, 9, 15, 16, 25]
# sqrts = [num**0.5 for num in numbers if num == int(num**0.5)**2 ]
# print(sqrts)

# #List of strings that contain all strings as lower case
# strings = ['Hello', 'WORLD', 'Python', 'PROGRAMMING']
# lower = [string.lower() for string in strings]
# print(lower)# ['hello', 'world', 'python', 'programming']

#List of numbers that contain each number multiplied by its index
# numbers = [10, 20, 30, 40, 50]
# multiplied = [num * i for i, num in enumerate(numbers)]
# print(multiplied)
# See how to use enumerate below
# fruits = ['apple', 'banana', 'mango']
# enumerate_fruits = list(enumerate(fruits))

# print(enumerate_fruits)  # Output: [(0, 'apple'), (1, 'banana'), (2, 'mango')]

#To change first letter to capital
# bicycles = ['treck', 'cannondale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}"
# print(message)

# motocycles = []
# motocycles.append('honda')
# motocycles.append('yamaha')
# motocycles.append('suzuki')
# print(motocycles)
# Usually the above is very useful as we do not know what list users will create

# motocycles = ['honda', 'yamaha', 'suzuki']
# poped_motocycle = motocycles.pop()
# print(poped_motocycle)
# print(motocycles)

#When you want to delete an item from a list and not use that item in any way,
# use the 'del' statement; if you want to use an item as you remove it use the pop()
# cars = ['bmw', 'audi', 'saburu']
# cars.sort(reverse = True)
# print(cars)

# squares = [value**2 for value in range(2,11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[:2]) # output is ['charles', 'martina'] Start slice from beginning of list
# print(players[4:]) # output is ['eli'] ens slice at the end of the list
# print(players[-3:]) # output is ['michael', 'florence', 'eli'] Counting is from backward
# #To Copy a list using slicing
# print(players[:]) # ['charles', 'martina', 'michael', 'florence', 'eli']
