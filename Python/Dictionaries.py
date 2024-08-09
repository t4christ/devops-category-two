#Dictionaries must have unique keys
# We access items in a dictionary with their keys as below
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(person["name"])  # Output: John
# #Adding new key:value pairs
# person['job'] = "Engineer"
# print(person) #Output {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Engineer'}

# #Delete item from Diction 
# del person['job']

# print(person)

# #To loop through a dictionary
# for key, value in person.items():
#     print(f"{key}: {value}")

# #To check if key is in the dictionay
# if "name" in person:
#     print("Name is in the dictionary")

# #To check number of items in a dictionary
# print(len(person))

#Using get() to access values: As usual we use keys to access values in dictionaries
# The probelm is that if the key does not exist we have error

# Using get() makes our program more robust and less likely to crash when the key is not found.
# person = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }

# print(person["profession"])  # Raises a KeyError

# print(person.get("profession"))  # Returns None

# print(person.get("profession", "Not provided"))  # Returns "Not provided" because we have set our custom message of "Not provided"

#To loop through all key-value pairs: Use .items()

# user_0 = {
#     'username' : 'efermi',
#     'first' : 'enrico',
#     'last' : 'fermi'
# }
# for key, value in user_0.items():
#     print(f"\nkey: {key}")
#     print(f"value: {value}")

#Looping through Only keys in dictionary
#Looping through keys is the default behaviour when looping through dictionary.

# for key in user_0.keys():# This will have the same output as for key in user_0
#     print(key.title()) 

#To loop through only values with no keys:
# for value in user_0.values:
#     print(value.title())

#List of Dictionaries

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

#Looping through a list of dictionary,creating a dictionary using range and using slicing on dictionary

# aliens = []
# for alien_number in range(30): #Returns series of numbers which just tells python how many times we want the loop to repeat
    # new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
    # aliens.append(new_alien) #We append each new alien to the empty list
#To show the 1st 5 aaliens out of the 30 created with slicing
# for alien in aliens[:5]:
#     print(alien)

#To modify the 1st 5 aliens using if, elif
#This is how to modify all the attributs in an object of a dictionary
# for alien in aliens[0:3]:
#     if alien['color'] == 'green'
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
#Note that the list should have an identical structure, so you can loop through the list and work with the objects in the same way.

#Looping through a List In a dictionary

favorite_languages = {
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'haskell']
}
for name, languages in favorite_languages.items():# meaning in everythin
    print(f"\n{name.title()}'s favorite languages are: ")
    for language in languages:#for the value part
        print(f"\t{language.title()}")