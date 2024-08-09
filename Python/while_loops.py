# While loop is used to keep a program runnings as long as certain conditions remain the same.
# While loops is followed by a condition. we can only break out of a while loop when the condition turns false.
# i = 0
# while i < 50:
#     print(i)
#     i+=1  #This is the condition to break the loop. Avoids infinite loops
#     #We can also have else block in a while loop as shown below:
# else:
#     print("done with all the work")

#When to use while loops or for loops?
#While loops are good for a long list of items that most times we do not know the end.
#While loops are good for looping for a long time. We do not know how long it's going to heppaen.
# while True:
#     response = input("say something: ")
#     if (response == 'bye'):
#         break

#while loops used for counting numbers from 1 to 5
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# We can make a program run for as long as a user wants it by running most of the program in a while loop
# We define a quite value and the program will continue to run for as long as the user have not entered that value

# prompt = "\nTell me something, and i will repeat it back to you: "
# prompt += "\nEnter 'quit to end the program. "

# message = " "
# while message != 'quit' :
#     message = input(prompt)
#     print(message)
# else:
#     print("Thanks for using my program")

# Side Note: The message we want to use in the while loop (or in our program) can be saved 
# Somewhere as a variable and then we just call it in the program without having to type it all out

#Using flag (True or fals)
# A flag is set when we have any of multiple things that can cause a program to stop running unlike in above that was just one
# All multiple things will be set to a flag (True or False). Once false the programs stops running

# prompt = "\nTell me something, and i will repeat it back to you: "
# prompt += "\nEnter 'quit to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == quit:
#         active = False
#     else:
#         print(message)

# Learning Point: When we have more than one condition to stop a program
# We use a flag to make the program True or False

#USING BREAK TO EXIT A LOOP
# Break is used to exit a code immediately without running the remaining code

#Example is the program below that asks users to enter cities they have been to

# prompt = "\nPlease enter the name of a city you have visited: "
# prompt += "\n(Enter 'quit' when you are finished.) " 

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city}.title()")

#LP: A while loop is an infinite loop unless something stops it
# We use break to quit any python loop (can be used to quit a for loop working through a list or dictionary) 
   
# number = 0
# while number < 6:
#     print(number)
#     number += 1
# else:
#     print("limit reached")

    #USE OF CONTINUE : Is used to return to the beginning of the loop based on the result
#of a conditional test

#For example a loop that counts from 1 to 10 but prints only the odd numbers

# odd_number = 0
# while odd_number < 10:
#     odd_number += 1
#     if odd_number % 2 == 0:
#         continue # Tells python to ignore and move to the beginning of the loop.
#     print(odd_number)

# Pizza Toppings Exercise page 123


while True: # Whiel True means keep doing the following action indefinitely until I explicitly tell you you to stop with a break statement or external interruption.
    age = input("please enter your age or 'quit' to exit: ")
    if age.lower() == 'quit':
        break
    try:     
        age_input = int(age)
    except:
        print("enter a valid input")
    if age_input < 3:
        print('movie is free for you')
    elif age_input <= 12:
        print('you will pay $10')
    else:
        print('Your ticket price is $15')

           

    #BELOW IS USING AN ACTIVE VARIABLE FOR THE ABOVE CODE

# active = True  # Step 1: Initialize an active variable

# while active:  # Step 2: Use the active variable in the loop condition
#     age = input("Please enter your age or 'quit' to exit: ")
#     if age.lower() == 'quit':
#         active = False  # Step 3: Update the active variable to stop the loop
#     else:
#         age_input = int(age)
        # Additional logic to process the age_input can be added here


     #USING WHILE LOOP WITH LIST AND DICTIONARIES

#Moving Items From one list to another