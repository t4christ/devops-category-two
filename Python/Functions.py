# # ### Functions in Python

# #Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable, and reducing redundancy. Here's a breakdown of how functions work in Python:

# ### Key Concepts

# #Function Definition**: Declaring a function using the `def` keyword.
# #Function Call**: Executing the function by its name followed by parentheses.
# #Parameters**: Inputs to the function, specified within the parentheses in the function definition.
# #Return Statement**: Outputs from the function, specified using the `return` keyword.




# # Define the function
# def add_numbers(a, b):
    
#     #This function takes two numbers as input and returns their sum.
    
#     result = a + b  # Perform the addition, the core logic, the task. Is the body of the code
#     return result   # Return the result

# # Call the function
# sum_result = add_numbers(5, 3)

# # Print the result
# print("The sum is:", sum_result)

# print((add_numbers(8, 2)))


# ### Explanation

# #1. **Function Definition**:
#  #   - `def add_numbers(a, b):` defines a function named `add_numbers` that takes two parameters `a` and `b`.
#  #   - The docstring `"""This function takes two numbers as input and returns their sum."""` describes what the function does.
#  #   - `result = a + b` performs the addition of the two parameters.
#  #   - `return result` returns the result of the addition.

# #2. **Function Call**:
#  #   - `sum_result = add_numbers(5, 3)` calls the `add_numbers` function with arguments `5` and `3`.
#   #  - The result of the function call is stored in the variable `sum_result`.

# #3. **Output**:
#  #   - `print("The sum is:", sum_result)` prints the result, which is `8`.

# ### Benefits of Using Functions

# #Modularity**: Break down complex problems into smaller, manageable pieces.
# #Reusability**: Write code once and reuse it multiple times.
# #Readability**: Make the code more organized and easier to understand.
# # Maintainability**: Simplify updates and bug fixes.


# list_of_dict = [{"name":"francis", "age":30}, {"name":"temitayo", "agr":30}]

# def get_employee():
#     for eachname in list_of_dict:
#         print(eachname)

# get_employee()

# def sum_numbers(a, b):
#     sum = a + b
#     print(sum)

# sum_numbers(-16, -4)


# list_of_dict = [{"name":"francis", "age":30}, {"name":"temitayo", "agr":30}]

# def get_maturity(age):
#     if age >= 18:
#         print(f"You are an adult")
#     elif age < 18:
#         print("You are a minor")
#     elif age < 5:
#         print("You are still a baby")
#     return "I'm done"

# print(get_maturity(1))



# list_of_dict = [{"name":"francis", "age":30}, {"name":"temitayo", "age":30}]

# def get_employee():
#     for eachname in list_of_dict:
#         print(eachname['name'])
#         print(eachname['age'])
#         return('done')

# print(get_employee())



# def get_name(name):
#     return (f"my name is {name}")

# print(get_name("Dibaal"))


# list_of_dict = [{"name":"francis", "age":30}, {"name":"temitayo", "age":30}, {"name":"success", "age":60}]

# def get_employee(list_of_dict):
#     for eachemployee in list_of_dict:
#         if eachemployee['age'] > 30:
#             print(eachemployee)

# get_employee(list_of_dict)

# list_of_students = ["success", "wale", "francis", "temitayo", "taiwo", "karen", "philip", "rogers", "williams", "adams"]
# #we want to right a program that assigns a unique number (1 to 10) to a list of students

# def assign_number(list_of_students):
#     count = 1
#     for name in list_of_students:
#         print(f"{name} you are assined number {count}")
#         count+=1

# assign_number(list_of_students)


#TO MAKE NUMBERS ASSIGNED RANDOM. USE THE RANDOM MODULE APRIL 17 TIME STAMP 1:32


# list_of_dict = [{"name":"francis", "age":25}, {"name":"temitayo", "age":39},{"name":"olawale", "age":23}, {"name":"success", "age":39}, {"name":"franca", "age":27}, {"name":"smith", "age":35}, {"name":"george", "age":42}]
# list_of_students = ["success", "wale", "francis", "temitayo", "taiwo", "karen", "philip", "rogers", "williams", "adam"]
# #on the fly we want to add each employees level base on their age and return the whole list back. we want their seniority base on their age. An excel sheet to return the list accordingly.

# def get_employee(list_of_dict):
#     index = 0
#     for eachname in list_of_dict:
#         if 20 < eachname["age"] < 30:
#             list_of_dict[index]["level"] = "Intermediate" #we are adding a key value to our list with key level and value Intermediate
#         elif 31 < eachname["age"] < 50:                     #we are adding a key value to our list with key level and value Senior
#              list_of_dict[index]["level"] = "Senior" 
#             #  print(index, eachname)
#         index+=1  
#     return list_of_dict 
            

# print(get_employee(list_of_dict))

#ANONYMOUS/INLINE FUNCTION: Functions with no Name. can have any number of parameters, but can only have 1 expression. They are concise way to create small, unnamed functions for short-term use. They are particularly useful when you need a simple function for short period and don't want to define a full function using def.
#Syntax: lambda argument: expression
#Example:

# def add(x,y):
#     return x + y
# print(add(7,9)) # To call the named function as we already Know

# #Equivalent of the above in anonymous/inline fumction is as below:
# add_num = lambda x,y: x+y # It's an anonymous function bc it has no Name
# print(add_num(7,9)) #This is how to call the anonymous function

# add_num = lambda x,y: x/y if x > y else "Division is invalid"
# print(add_num(7,9)) #Division is invalid
# print(add_num(8, 7)) #1.1428571

#Lambda function to only validated 4 character lenght names

# name_char = lambda name: f"your {name} is valid" if len(name) >=4 else f"your {name} is invalid"
# print(name_char("olas"))





        
        







