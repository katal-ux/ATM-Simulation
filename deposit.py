import utils 

def deposit():
    x=int(input("Enter a amount:"))
    utils.balance += x
    utils.transactions.append({"credited":x})
    print(f"amount {x} has been deposited in your account")