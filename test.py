import datetime

bank_balance = 6000
salary = 3000

def salary_arrived():
    # your code here
    global bank_balance
    if datetime.datetime.now().day ==6:
        bank_balance += salary

    print("bank balance: ", bank_balance)


salary_arrived()