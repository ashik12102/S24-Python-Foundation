import datetime

bank_balance = 6000
salary = 3000
salary_drawn_count = 1

def salary_arrived():
    # your code here
    global bank_balance
    global salary_drawn_count
    if datetime.datetime.now().day ==6:
        bank_balance += salary
        salary_drawn_count+=1

    print("bank balance: ", bank_balance)


salary_arrived()

def add_bonus():
    # your code here
    global bank_balance
    bonus = int(input("Enter the bonus amount received: "))
    bank_balance += bonus

    print("bank balance after bonus: ", bank_balance)
add_bonus()
