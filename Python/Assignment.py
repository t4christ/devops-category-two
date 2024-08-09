# # Add salary to employee record
# def add_salary(records, name, age, salary):
#     records[name] = {"name": name, "age": age, "salary": salary}
#     return records

# # Update salary based on age
# def update_salary(records):
#     for record in records.values():
#         if 20 <= int(record['age']) <= 30:
#             record['salary'] = str(int(record['salary']) + 10000)
#         elif 31 <= int(record['age']) <= 50:
#             record['salary'] = str(int(record['salary']) + 20000)
#     return records

# # Lambda function to check age
# check_age = lambda records: records[list(records.keys())[0]] if int(records[list(records.keys())[0]]['age']) > 30 else "Age not greater than 30"

# # Usage
# employee_records = {}
# employee_records = add_salary(employee_records, "success", "30", "10000")
# employee_records = update_salary(employee_records)
# first_record_check = check_age(employee_records)


import re
bank_record_db = [{"bank":"providus","account_numbers":["3456789110", "3456239110", "3456789110"]},# List of dictionaries with each dictionary representing a bank and contains 2 keys, bank and account_numbers
               {"bank":"zenith","account_numbers":["3556789110", "3556239110", "3556789110"]}, # The key is bank and it's value is a string that represents the bank name and the 2nd key is account_numbers and it's value is a list of account numbers
               {"bank":"gtb","account_numbers":["3656789110", "3656239110", "3656789110"]},] # For each dictionary the key bank has the value representing the bank name and the 2nd key account_numbers has the value representing the account numbers.
                           


# def check_bank_validity(account_no, bank_record=[]):
#     # Check if account_no is None or empty
#     if not account_no:
#         return "Account number cannot be empty"

#     # Check if account_no is a string of digits
#     if not account_no.isdigit():
#         return "Account number must be a string of digits"

#     # Check if account_no is a 10-digit number
#     pattern = r'^\d{10}$'
#     if not re.match(pattern, account_no):
#         return(f"Your account number {account_no} is not a 10-digit number")

#     # Check if account_no is in bank records
#     for number in bank_record:
#         if account_no in number['account_numbers']:
#             return (f"Your account number {account_no} from {number["bank"]} bank is valid")

#     return(f"Your account number {account_no} is invalid")

# # Get account number from user
# while True:
#     account_no = input("Please enter your trusted account number: ")
#     result = check_bank_validity(account_no, bank_record)
#     if "invalid" not in result:
#         break
#     else:
#         print(result)

# print(result)

def get_bank_codes(bank_record_db):#This is a function to try to get just the 1st 2 digit from each bank, the unique feature of all the banks.
    bank_codes = []
    for bank_dictionary in bank_record_db: #bank dictionary here is a placholder holding each of the bank dictionaries, one at a time as we iterate over the bank_record_db
        bank_codes += [b[:2] for b in bank_dictionary["account_numbers"]] #Used slicing list comprihension to pick the 1st 2 digits from each account numbers and fill up the empty bank_codes
    return list(set(bank_codes)) #We used set to ensure we avoid repeated 2 digits and the we change back to list

bank_code = get_bank_codes(bank_record_db) #To get bank code we call the get_bank_codes function and pass in the bank_record_db

def check_bank_validity(account_no, bank_code=[],bank_record_db=[]):# The empty list allows the function to be called with or without arguments for bank_code and bank_record_db
    
    if account_no[:2] not in bank_code:
        return("Account number is an invalid bank_code")
    
    if not account_no.isdigit():
        return("Account number is invalid. it should be 10 digits")
    
    if len(account_no) != 10:
        return("Account number is not up to 10 digits")
    
    
    
   
    
    for account_number in bank_record_db:
        if account_no in account_number['account_numbers']:
            return (f"Your account number {account_no} from {account_number["bank"]} bank is valid")
    return(f"Your account number {account_no} is invalid")

while True:
    account_no = input("Please enter your trusted account number: ")
    result = check_bank_validity(account_no, bank_code, bank_record_db)
    print(result)
    if "valid" in result:
        while True:
            user_response = input("Do you want to perform another operation? (Yes/No): ")
            if user_response.lower() == "yes":
                print("We will get back to you")
                break
            elif user_response.lower() == "no":
                print("Thank you for banking with us")
                break
            else:
                print("Invalid response. Please answer with Yes or No.")
        break  # This will break the outer loop
    else:
        # print("Invalid account number. Please try again.")
        print(result)