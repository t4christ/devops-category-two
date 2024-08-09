def calculate_addition(x,y):
    return x+y

def calculate_multiplication(x,y):
    return x*y

def calculate_account_balance(x,y):

    if y > x + 10:
        return "Error! Sorry, you've gone above your overdraft"
    else:
        print(x-y) 

#Function To Approve Overdraft if  x > 100

# def approve_overdraft(x, y):
#  # Check if the balance is sufficient to cover the withdrawal without overdraft   
#     if x > 100: 
#         if y > x + 10:
#             return "Error! Sorry, you've gone above your overdraft"
#         else:
#             return x - y
#     else:
#         if y > x:
#             return "Error! Sorry, you've gone above your overdraft"
#         else:
#             return x - y    
    
# def approve_overdraft(x, y):
#     # Check if the balance is sufficient to cover the withdrawal without overdraft
#     if x >= 100: 
#         if y > x + 10:
#             return "Error! Sorry, you've gone above your overdraft"
#         else:
#             return x - y
#     else:
#         return "Error! Your balance must be at least 100 to allow overdraft"

# def request_loan(user_balance):
#     loan_amount = 100000
#     minimum_balance = 200000

#     if user_balance >= minimum_balance:
#         return f"Loan of {loan_amount} Naira approved."
#     else:
#         return f"Loan denied. You must have at least {minimum_balance} Naira in your account to qualify for a loan."

# def request_loan(user_balance, loan_amount):
#     minimum_balance = 200000

#     if user_balance >= minimum_balance:
#         return f"Loan of {loan_amount} Naira approved."
#     else:
#         return f"Loan denied. You must have at least {minimum_balance} Naira in your account to qualify for a loan."

def create_customers(num_customers):
    return [{'name': f'Customer{i}', 'balance': i*100-500} for i in range(1, num_customers+1)]

def check_balances(customers):
    for customer in customers:
        if customer['balance'] < 0:
            customer['debt_account'] = True
        else:
            customer['debt_account'] = False

def grant_overdrafts(customers):
    for customer in customers:
        if not customer.get('debt_account', False):
            customer['overdraft_eligibility'] = 100000
        else:
            customer['overdraft_eligibility'] = 0

def print_customers(customers):
    for customer in customers:
        print(f"Name: {customer['name']}, Balance: {customer['balance']}, Overdraft Eligibility: {customer['overdraft_eligibility']}")

# Create a list of 10 bank customers
customers = create_customers(10)

# Check their balances and mark as debt account if balance is less than 0
check_balances(customers)

# Grant overdraft eligibility to customers not marked as debt account
grant_overdrafts(customers)

# Print the customers' names, balances, and overdraft eligibilities
print_customers(customers)