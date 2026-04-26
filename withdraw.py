import utils 
def with1():
    x=int(input("Enter the amount you want to withdraw:"))
   
    if x > utils.balance:
        print("Insuffecient balance")
    else:
        utils.balance -=x
        utils.transactions.append({"debited" : x})
        print("Withdrawal successful")

