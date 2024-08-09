bank_record_db = [{"bank":"providus","account_numbers":["3456789110","3456239110","3456109110"]},
               {"bank":"zenith","account_numbers":["3556789110","3556239110","3556109110"]},
               {"bank":"gtb","account_numbers":["3656789110","3656239110","3656109110"]},
               {"bank":"ecobank","account_numbers":["3756789110","3756239110","3756109110"]},
               {"bank":"firstbank","account_numbers":["3856789110","3856239110","3856109110"]}
]


# def get_bank_codes(bank_record_db):
#     bank_codes = []
#     for bank in bank_record_db:
#         bank_codes +=[b[0:2] for b in bank["account_numbers"]]
#     return list(set(bank_codes))

# bank_code = get_bank_codes(bank_record_db)

# def check_bank_validity(account_no,bank_code=[],bank_record_db=[]):
#     if len(account_no) != 10:
#         print("Account number is invalid, ten digits required")
#         return False

    
#     if not account_no.isdigit():
#         print("Account number should be a valid ten digits number")
#         return False


#     if account_no[:2] not in bank_code:
#         print("Account number is not a valid bank code")
#         return False

#     for account_number in bank_record_db:
#         if account_no in account_number["account_numbers"]:
#             print(f"Your account number {account_no} is valid from {account_number['bank']} bank")
#             return True
#     print(f"Account number {account_no} is invalid")
#     return False

# def check_valid_no(check_result):
#         other_request = input("Your account number is valid. Any other requests: ")
#         if other_request.lower() == "yes":
#             print("We will get back to you on other list of services we offer")
#         elif other_request.lower() == "no":
#             print("Thank you for banking with us. Have a nice day")
#         return check_result

# while True:
#     failed_attempts = 3
#     account_no = input("Please enter your account number:  ")
#     check_result = check_bank_validity(account_no,bank_code,bank_record_db)
#     if check_result:
#         check_valid_no(check_result)
#         break
#     elif not check_result:
#         while failed_attempts > 0:
#             account_no = input("Please enter a valid account number:  ")
#             check_result = check_bank_validity(account_no,bank_code,bank_record_db)
#             if check_result:
#                 check_valid_no(check_result)
#             elif not check_result:
#                     failed_attempts -=1
#             elif failed_attempts > 0:
#                 print(f"You have  {failed_attempts} attempts left")
                    
#         else:
#             print("You have been temporarily blocked after too many attempts. Pls try again after hone hour")
#     break
# for bank in bank_record_db:
#  result = [b for b in bank["account_numbers"]]
#  print(result)

# for bank in bank_record_db:
#     for key, value in bank.items():
#        print(f"{key}:{value}")


