# import json
# #To load/Read a File

# read_json = "example.json"
# write_json = "foundations.json"

# with open(read_json, "r") as file:
#     data = json.load(file)
#     print(data)

#To write to a file

# data = {
# "name" : "Dibaal" # We want to write this data into "foundations.json"
# }

# with open(write_json, "w") as file:
#     try:
#         json.dump(data, file, indent=4)
#     except:
#         print("Error while writing to file")

# import json

# write_json = "foundations.json"

# data = [{"name":"francis", "age":25}, {"name":"temitayo", "age":39},{"name":"olawale", "age":23}, {"name":"success", "age":39}, {"name":"franca", "age":27}, {"name":"smith", "age":35}, {"name":"george", "age":42}]
    
# with open(write_json, "w") as file:
#     try:
#         json.dump(data, file, indent=4)
#     except:
#         print("Error while writing to file")



# In the version of the code below we want only the objects with food copied/written into the json file.
import json

write_json = "foundations.json"

data = [{"name":"francis", "age":25, "food":["abula","yam","beans"]}, {"name":"temitayo", "age":39},{"name":"olawale", "age":23}, {"name":"success", "age":39,"food":["rice","pizza","plantain"]}, {"name":"franca", "age":27}, {"name":"smith", "age":35}, {"name":"george", "age":42}]
    
with open(write_json, "w") as file:
    try:
        food_entry_list = []
        for food_entry in data:
            if "food" in food_entry:
                food_entry_list.append(food_entry)
        json.dump(food_entry_list, file, indent=4)
    except:
        print("Error while writing to file")
