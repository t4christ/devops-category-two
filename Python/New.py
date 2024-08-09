# class person:
#     def __init__(self, name, country):
#         self.name = name
#         self.country = country
# person = person('Dibaal', 'UK')
# print(person.name)
# print(person.country)

# name = 'johnny'
# age = 55
# print(f'hi {name}. You are {age} years old')

# selfish = 'me me me'
# print(selfish[4])




# selfish = [0,1,2,3,4,5,6,7]
# print(selfish[0:2])
# print(selfish[0:8:2])
# print(selfish[::-1])
# new_list = selfish.append(100)
# print(new_list)
# name = 'ade'
# age = 50 
# village = 'okana'
# print(f'{name}'is {age} years old')
# matrix = [1, 3, 6, 'a']
# matrix2 = [2, 100, 'a']
# new_matrix = matrix.append(100)
# print(matrix)
# matrix.extend(matrix2)
# matrix.pop(2)
# matrix.clear()
# print('a' in matrix )

# print(matrix.count('a'))
# print(len(matrix))
# print(matrix[::-1])
# weapons = None
# print(weapons)
#Allows us to retrieve the value of a specified key from a dictionary. If 
# alien_o = {'color':'green','speed':'slow'}
# point_value = alien_o.get('points', 'No point value assigned')
# print(point_value)
# point_value = alien_o.get('speed', 'No point value assigned')
# print(point_value)

# The line `point_value = alien_o.get('color' 'No point value assigned')` is not working as expected because there's a missing comma between `'color'` and `'No point value assigned'`. 

# The `get` method in Python is used to retrieve the value of a specified key from a dictionary. It takes two parameters: the key you want to retrieve, and a default value to return if the key is not found in the dictionary.

# Here's the corrected code:

# ```python
# alien_o = {'color':'green','speed':'slow'}
# point_value = alien_o.get('color', 'No point value assigned')
# print(point_value)  # Outputs: 'green'
# dictionary = {'a': 1, 'b': 2, 'c': 3}
# print(dictionary.get('a'))
#      or
#  print(dictionary['a'])
# user = {
#   'basket': [1, 2, 3],
#   'greet': 'hello',
#   'age': '20'
#  }  
# print('hello' in user.keys())  
# print('age' in user.values()) 
# user2 = user.copy()
# print(user)
# print(user2) 

# my_tuple = (1, 2, 3, 2)    
# print(my_tuple.count(2)) 
# print(my_tuple.index(3)) 

# my_set = {1, 2, 3, 4, 5, 5}
# print(my_set)

#Functions
# def add_numbers(num1, num2):
#     result = num1 + num2
#     return result

# output = add_numbers(3, 4)
# print(output)  # Outputs: 7

# def greet():
#     print("Hello, world!")

# greet()  # Outputs: Hello, world!

# def greet(name, greeting="Hello"):
#     print(f"{greeting}, {name}!")
    
# greet('Zeb', 'what happened to you')

# for x in range(0,10):
#     print(x)

#LAMBDA FUNCTIONS
# add = lambda x, y: x + y
# print(add(5, 3)) 

# numbers = [1, 2, 3, 4, 5]
# squares = map(lambda x: x ** 2, numbers)
# print(list(squares))  # Outputs: [1, 4, 9, 16, 25]


# f = open("test.txt", 'w')
# f.write("Hello, world!")  # Writes "Hello, world!" to the file
# f.close()

# f = open("test.txt", 'r')
# print(f.read())  # Reads and prints the content of the file
# f.close()

# import os

# Check if file exists
# if not os.path.isfile('file.txt'):
    # If it doesn't exist, create a new file
    # with open('file.txt', 'w') as f:
    #     pass

# Create a file with 30 lines
# with open('lines.txt', 'w') as f:
#     for i in range(30):
#         f.write('She is on line number {}\n'.format(i + 1))

# Read the file and replace "She" with "He"
# with open('lines.txt', 'r') as f:
#     lines = f.readlines()

# with open('lines.txt', 'w') as f:
#     for line in lines:
#         f.write(line.replace('She', 'He'))



# import re

# def valid_mastercard(number):

#     pattern = r'^(5[1-5][0-9]{14})$'
    
#     match = re.match(pattern, str(number))
#     return match is not None


# print(valid_mastercard(1615141312100908))  
 
  



# import re

# # Define the string
# text = "Hello, my name is John cba Doe and my email is john.doe@example.com"

# # Define the literal pattern
# pattern = "abc"

# # Use re.search() to search the string for the pattern
# match = re.search(pattern, text)

# # If a match is found, print it
# if match:
#     print("Match found:", match.group())
# else:
#     print("No match found")

# import re

# text = "My name is Dibaal and the name of my Dad is Dibaal"

# pattern = r'Dibaal'

# # watch = re.findall(pattern, text)
# watch = re.search(pattern, text)


# print("matches found:", watch)
# print("matches found:", watch)

# import re
# pattern = r"name"
# text = "my name is Dibaal and my Mum's name is Iberaan"

# match = re.findall(pattern, text)
# print(len(match))

# print("Number of matches found:",len(match))

# REGEX WITH FUNCTIONS

# import re

# user_input = "I have a Tesla car " # This to be passed to the function

# def check_car_inventory(user_input):  #Function with the user input passed
#     pattern = r"car"
#     check_car_inventory = re.findall(pattern, user_input)

#     if len(check_car_inventory) < 2:
#         print("He has a car")
#     else:
#         print(f"He has {len(check_car_inventory)} cars")

# check_car_inventory(user_input)

# In your specific code, the function `check_car_inventory()` takes a 
#string as input, finds all occurrences of the word "car", and then prints 
#a message based on the number of occurrences. This functionality is encapsulated 
#within the function, making it easy to reuse and maintain.

#CODE TO VALIDATE PHONE NUMBER WITH REGEX

# import re

# def validate_phone_number(phone_number):
#     pattern = r'^\+44-\d{3}-\d{3}-\d{4}$'

    # if re.match(pattern, phone_number): # phone_number does not throw an error even when
        # print("Valid UK number")        # not defined at this poin bc python only executes
    # else:                               # when it's been called
#         print("Invalid phone number. A UK number is required")

# phone_number = "+44-300-500-7899"

# validate_phone_number(phone_number)

# EMAIL VALIDATION WITH REGEX

# import re

# def validate_email(email_address):
#     pattern = r'^[a-z0-9]+@[a-z]+\.[a-z]{2,}$'

#     if re.match(pattern, email_address):
#         print("Valid email address")
#     else:
#         print("Invalid email address")
# email_address = "dibaal4real@yahoo.com"
# validate_email(email_address)

# VALIDATE MASTER CARD NUMBER WITH REGEX
# import re
# def valid_mastercard(number):
#     pattern = r'^(5[1-5][0-9]{14})$'
#     if re.match(pattern, number):
#         print("Valid mastercard number")
#     else:
#         print("Invalid mastercard number")
# number = "539123456789129990"
# valid_mastercard(number)

#TO IST CHECK IF NUMBER IS UP TO 16 DIGITS 
# import re
# def valid_mastercard(number):
#     pattern = r'^(5[1-5][0-9]{14})$'
#     if len(number) > 16 or len(number) < 16:  #First of all check for the lenght b4 even doing anything
#         return("Invalid mastercard digit lenght")
#     if re.match(pattern, number):
#         return("Valid mastercard number")
#     else:
#         return("Invalid mastercard number")
# number = "539123456789129990"
# print(valid_mastercard(number))

# import re

# bank_record = [{"bank":"providus","account_numbers":["3456789110", "3456239110", "3456789110"]},# List of dictionaries with each dictionary representing a bank and contains 2 keys, bank and account_numbers
#                {"bank":"zenith","account_numbers":["3556789110", "3556239110", "3556789110"]}, # The key is bank and it's value is a string that represents the bank name and the 2nd key is account_numbers and it's value is a list of account numbers
#                {"bank":"gtb","account_numbers":["3656789110", "3656239110", "3656789110"]},] # For each dictionary the key bank has the value representing the bank name and the 2nd key account_numbers has the value representing the account numbers.
#                                                                                             #bank is a dictionary but, bank_record is a list of the bank dictionaries.
# def flatten_accounts(bank_record):
#     final_records = [] # Empty list to store the account numbers from bank_record
#     for bank_info in bank_record:# bank_info is a placeholder holding the dictionary one at a time while looping through the list of dictionaries
#         final_records += bank_info["account_numbers"] # This is accessing the value associated with the key Just to get the account numbers

#     return final_records # return statement is whatallows a function to produce a result that can be stored in a variable or printed out.
# ##print(flatten_accounts(bank_record)) #This is only useful if we want to see the list of account numbers ie the final_records



# def check_bank_validity(account_no, bank_record=[]):
    
#     account_numbers = flatten_accounts(bank_record) #This gives us the list we generated above ie the final_records list. The above function is called here.
#     for each_number in account_numbers: #Iterating through the list of account numbers
#         matches = re.findall(each_number, account_no) #each_number is like the pattern and account_no is the string (text) to be searched
#         if len(matches) == 1:
#             return(f'Your account number {account_no} is valid')
#     return(f"Your account number {account_no} is invalid")
# print(check_bank_validity("3456789110"))




import re

bank_record = [{"bank":"providus","account_numbers":["3456789110", "3456239110", "3456789110"]},# List of dictionaries with each dictionary representing a bank and contains 2 keys, bank and account_numbers
               {"bank":"zenith","account_numbers":["3556789110", "3556239110", "3556789110"]}, # The key is bank and it's value is a string that represents the bank name and the 2nd key is account_numbers and it's value is a list of account numbers
               {"bank":"gtb","account_numbers":["3656789110", "3656239110", "3656789110"]},] # For each dictionary the key bank has the value representing the bank name and the 2nd key account_numbers has the value representing the account numbers.
                                                                                            #bank is a dictionary but, bank_record is a list of the bank dictionaries.
def flatten_accounts(bank_record):
    final_records = [] # Empty list to store the account numbers from bank_record
    for bank_info in bank_record:# bank_info is a placeholder holding the dictionary one at a time while looping through the list of dictionaries
        final_records += bank_info["account_numbers"] # This is accessing the value associated with the key Just to get the account numbers

    return final_records # return statement is what allows a function to produce a result that can be stored in a variable or printed out.



def check_bank_validity(account_no, bank_record=[]):
    for bank in bank_record:
        for account_number in bank["account_numbers"]:
            if account_no == account_number:
                return (f'Your account number {account_no} is valid and the bank is {bank["bank"]}')
    return(f"Your account number {account_no} is invalid")

print(check_bank_validity("3456789110", bank_record))



