#WORKING WITH OTHER FILE OTHER THAN TXT
#CSV files = Comma-separated Values file
# Each line in a csv file correspond to a row in the table, each field in the row is separated by a comma
#Headers: The 1st line often contains headers, which are the names of the columns

#READING A CSV FILE:
# import csv # provides functionality to read and write to CSV files.

# csv_filename = "foundations.csv"

# with open(csv_filename, "r") as file:
#     reader = csv.reader(file) #The csv.reader function takes the file object as an argument and returns a reader object. This reader object can be used to itrrate over the rows in the csv file, where each row is returned as a list of strings. Is part of the python's csv module.
#     for row in reader:
#         print(row)

#writing to a csv file (example.csv) : we want to write to a csv file

# csv_filename = "dibaal.csv"


# with open(csv_filename, 'w', newline='') as file: #The newline argument is used to prevent extra newline characters from being added on some platforms.
#     csv_writer = csv.writer(file) #Creates a csv_writer object that will be used to write to the csv file.
#     csv_writer.writerow(['Name', 'Age', 'Occupation']) #Writes rows to the csv file using csv_writer.writerow
#     csv_writer.writerow(['Alice', '30', 'Engineer'])
#     csv_writer.writerow(['Bob', '25', 'Designer'])
#     csv_writer.writerow(['Charlie', '35', 'Teacher'])



# import csv
# write_csv_filename = "foundations1.csv" # Name of csv file that will be written to.

# get_csv_filename = "example.csv" #Name of csv file to be read.

# data = [["Name", "Age", "Country"], 
#         ["Success", 30, "Nigeria"]
#         ["Dibaal", 60, "UK"]
#         ]

# with open(write_csv_filename, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
    


#TO DYNAMICALLY READ AND WRITE TO A CSV FILE USE THE BELOW WITH FUNCTIONS




# import csv
# write_csv_filename = "foundations1.csv" # Name of csv file that will be written to.

# get_csv_filename = "example.csv" # Name of csv file that will be read from.

# def get_csv(csv_filename):# This function takes a filename as an argument and reads the contents of the CSV file.
#     result = []
#     with open(csv_filename, "r") as file: #Opens the file in read mode
#         reader = csv.reader(file) #Uses csv reader to read the file row by row
#         for row in reader: #Iterates overs each row
#             result.append(row) # Each row is appended to the result list.
#     return result # The function returns the result list, which contains all the rows from the csv file.

# with open(write_csv_filename, "w", newline='') as file: #Opens the csv file (foundations1.csv) in write mode
#     writer = csv.writer(file) # a csv.writer object is created to write to the file. Think of csv.writer(file) as creating a special pen (writer) that you can use to write data into a notebook(file), where the notebook is a csv file.
#     writer.writerows(get_csv(get_csv_filename)) # The "writer.writerows" method is used to write multiple row to the sv file.
