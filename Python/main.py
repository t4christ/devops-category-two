# import Assignment
# Assignment.display('Sample message', True)

# from Assignment import display
# display('Sample message')

# list_of_dict = [{'name': 'success', 'age': '30', 'salary': '10000'}, {'name': 'failure', 'age': '20', 'salary': '10000'}]
# print((list_of_dict)[0]["name"])




# import os

# # To Check if the file file.txt exists

# with open('line.txt', 'w') as f:
#     for i in range(30):
#         f.write('She is on line number {}\n'.format(i + 1))


# import json

# data = [
#     {"name":"dibaal","age":25,"food":["abula","yam","beans"]},
#     {"name":"temitayo","age":39},
#     {"name":"olawale","age":23},
#     {"name":"success","age":39,"food":["rice","abula","pupuru"]},
#     {"name":"franka","age":27},
#     {"name":"smith","age":35},
#     {"name":"george","age":42}
# ]



# selected_records = [record for record in data if "food" in record]
# print(selected_records)

# written_records = selected_records

# with open('selected_records.json', 'w') as file:
#     json.dump(written_records, file)

# import json

# data = [
#     {"name":"dibaal","age":25,"food":["abula","yam","beans"]},
#     {"name":"success","age":39,"food":["rice","abula","pupuru"]},
#     {"name":"temitayo","age":39},{"name":"olawale","age":23},
#     {"name":"franka","age":27},
#     {"name":"smith","age":35},{"name":"george","age":42}
# ]

# def check_food(filename, check_food_status):
#     with open(filename, "w") as file:
#         try:
#             filtered_data = [d for d in data if ("food" in d) == (check_food_status == "checkfood")]
#             json.dump(filtered_data, file, indent=4)
#         except:
#             print("Error while writing to file")

# check_food("food.json", "checkfood")
# check_food("nofood.json", "dontcheckfood")

# class planet:
#     def __init__(self, population, size):
#         self.population = population
#         self.size = size
#     def inhabited(self):
#         print(f"This planet has {self.population} people and it's {self.size} big")

# mars = planet("fifty", "eighty")
# saturn = planet("twenthy", "hundredKM")

# mars.inhabited()
# saturn.inhabited()

# class worlds(planet):
#     def war(self):
#         print(f"The world has {self.population} and it's {self.size} big)")

# first_war = worlds("80,000", "40,000")

# first_war.war()

class Smartphone:   #PARENT CLASS
    def __init__(self, manufacturer, model):
        self.manufacturer = manufacturer
        self.model = model

    def phone_boot_sound(self):
        print(f"{self.model} was made by {self.manufacturer} ")

class Tablet(Smartphone):       #TABLET IS A SUBCLASS OF Smartphone.Demonstrating Inheritance
    def phone_boot_sound(self):   #Inherited manufacturer and model attributes from Smartphone
        print(f"{self.model} was made by {self.manufacturer} showing inheritance")

# OBJECTS: Creating Instances of the classes
Iphone = Smartphone("Apple", "Iphone14")
Samsung = Smartphone("Samsung", "Samsung14")
Windows = Smartphone("Windows", "Windows14")
Google = Smartphone("Google", "Google14")
Ipad = Tablet("Apple", "Iphone14")

#Polymorphism: Thesame method, 'phone_boot_sound' behaves differently depending on the class
Iphone.phone_boot_sound()
Samsung.phone_boot_sound()
Windows.phone_boot_sound()
Google.phone_boot_sound()
Ipad.phone_boot_sound()
Ipad.phone_boot_sound()


# Ipad = Tablet("Apple", "Iphone14")

# Ipad.company_tablet()
# Ipad.phone_boot_sound()




































































































































































































































































































































































































































































