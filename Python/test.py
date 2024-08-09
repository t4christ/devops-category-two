# import re

# bank_record = [{"bank":"providus","account_numbers":["3456789110", "3456239110", "3456789110"]},# List of dictionaries with each dictionary representing a bank and contains 2 keys, bank and account_numbers
#                {"bank":"zenith","account_numbers":["3556789110", "3556239110", "3556789110"]}, # The key is bank and it's value is a string that represents the bank name and the 2nd key is account_numbers and it's value is a list of account numbers
#                {"bank":"gtb","account_numbers":["3656789110", "3656239110", "3656789110"]},] # For each dictionary the key bank has the value representing the bank name and the 2nd key account_numbers has the value representing the account numbers.
#                                                                                             #bank is a dictionary but, bank_record is a list of the bank dictionaries.
# # def flatten_accounts(bank_record):
# #     final_records = [] # Empty list to store the account numbers from bank_record
# #     for bank_info in bank_record:# bank_info is a placeholder holding the dictionary one at a time while looping through the list of dictionaries
# #         final_records += bank_info["account_numbers"] # This is accessing the value associated with the key Just to get the account numbers

# #     return final_records # return statement is what allows a function to produce a result that can be stored in a variable or printed out.



# def check_bank_validity(account_no, bank_record=[]):
#     for number in bank_record:
#         pattern = r'\d{10}'
#         if account_no in number['account_numbers'] and re.match(pattern, account_no):
#             return (f'Your account number {account_no} from {number["bank"]} bank is valid')
#     return(f"Your account number {account_no} is invalid")
# account_no = input("Please enter your trusted account number: ")
# print(check_bank_validity(account_no, bank_record))


bank_record_db = [{"bank":"providus","account_numbers":["3456789110","3456239110","3456109110"]},
               {"bank":"zenith","account_numbers":["3556789110","3556239110","3556109110"]},
               {"bank":"gtb","account_numbers":["3656789110","3656239110","3656109110"]},
               {"bank":"ecobank","account_numbers":["3756789110","3756239110","3756109110"]},
               {"bank":"firstbank","account_numbers":["3856789110","3856239110","3856109110"]}
]


def get_bank_codes(bank_record_db):
    bank_codes = []
    for bank in bank_record_db:
        bank_codes +=[b[:2] for b in bank["account_numbers"]]
    return list(set(bank_codes))

bank_code = get_bank_codes(bank_record_db)

def check_bank_validity(account_no,bank_code=[],bank_record_db=[]):
    if len(account_no) != 10:
        print("Account number is invalid, ten digits required")
        return False

    
    if not account_no.isdigit():
        print("Account number should be a valid ten digits number")
        return False


    if account_no[:2] not in bank_code:
        print("Account number is not a valid bank code")
        return False

    for account_number in bank_record_db:
        if account_no in account_number["account_numbers"]:
            print(f"Your account number {account_no} is valid from {account_number['bank']} bank")
            return True
    print(f"Account number {account_no} is invalid")
    return False

def check_valid_no(check_result):
        other_request = input("Your account number is valid. Any other requests: ")
        if other_request.lower() == "yes":
            print("We will get back to you on other list of services we offer")
        elif other_request.lower() == "no":
            print("Thank you for banking with us. Have a nice day")
        return check_result

wrong_number = []

while True:
    account_no = input("Please enter your account number:  ")
    check_result = check_bank_validity(account_no, bank_code, bank_record_db)
    if check_result:
        check_valid_no(check_result)
        break
    else:
        wrong_number.append(account_no)
    if len(wrong_number) < 5:
            continue
     else:
        print("You have been temporarily blocked for too many wrong entries")
            break