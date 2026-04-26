from deposit import deposit
from displaybalance import disp
from statement import state
from withdraw import with1

def Atm():
    while True:
        print("\n1. Withdraw")
        print("\n2. Deposit")
        print("\n3. Display Balance")
        print("\n4. Show Statement")
        print("\n5. Exit")
        choice =input("Enter your choice: ")
        if choice.isdigit(): 
            choice=int(choice)
            if choice == 1 : 
               with1()
            elif choice ==2 : 
                deposit()
            elif choice == 3:
                disp()
            elif choice ==4 :
                state()
            elif choice==5:
                print("Loggin off!")
                break
            else :
                print("Invalid input")            
    
    
Atm()
