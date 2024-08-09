# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# #Conditional Test
# requested_topping = 'mushrooms'

# if requested_topping != 'anchoves':
#     print('Hold the Anchovies')

# #Checking multiple conditions using 'and' keyword

# #We can check if two people are over 21
# age_0 = 22
# age_1 = 18
# print(age_0 and age_1 >= 21) # False

# #Checking if a value is in a list or not
# banned_users = ['andrew' 'carolina' 'David']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a respons if you wish")

# car = 'subaru'
# print(car == 'subaru') # I predict True
# print(car == 'Subaru') # P False

# age = 12
# if age < 4:
#     price = 0
# elif age < 10:
#     price = 25
# else:
#     price = 20
# print(f"Your admission cost is ${price}.")

# alien_color = ['white', 'yellow', 'red']
# if 'green' in alien_color:
#     print("You have earned 5 points")
# if 'yellow' in alien_color:
#     print("You have earned 10 points")
# if 'red' in alien_color:
#     print("You have earned 15 points")

#when the name of a list is used in an if statement,
#Python returns 'True'  if the statement contain atleast one item
#An empty list evaluates to False. See below:

# requested_toppings = []

# if requested_toppings: #Returns True if it has ab item
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")

#Using Multiple List:

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'peperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {'requested_topping'}.")
#     else:
#         print(f"Sorry, we don't have {'requested_topping'}")
# print('\nFinished making your pizza')

#BOOK EXERCISES ON LIST if statements

usernames = []

# if usernames:
#     for username in usernames:
#         if username == 'admin':
#             print(f"Hello {username}, would you like to see a status report?")
#         else:
#             print(f"Hello {username}, thank you for logging in again.")
# else:
#     print("We need to find some users!")

#If is used when you want to perform an action based
#on condition
#for is used when you want to perform an action for each item in
#a sequence or other iterable object.

#To create a program that simulates how websites ensure that everyone has a unique username

# current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
# new_users = ['user1', 'nuser1','nuser2', 'nuser3','user5']

# for user in new_users:
#     if user in current_users:
#         print(f"The username {user} is already taken, pick something different")
#     else:
#         print(f"{user} is available for use, thankyou!")

#To make sure Comparsim is case sensitive:
# current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
# new_users = ['user1', 'nuser1','nuser2', 'nuser3','user5']

# # Create a new list with lowercase and uppercase versions of all users
# current_users_lower_upper = [user.lower() for user in current_users] + [user.upper() for user in current_users]

# for user in new_users:
#     if user.lower() in current_users_lower_upper or user.upper() in current_users_lower_upper:
#         print(f"The username {user} is already taken, pick something different")
#     else:
#         print(f"{user} is available for use, thankyou!")

# numbers = list(range(1,10))

# for number in numbers:
#     if number == 1:
#         print(f"{number}st")
#     elif number == 2:
#         print(f"{number}nd")
#     elif number == 3:
#         print(f"{number}rd")
#     else:
#         print(f"{number}th")

