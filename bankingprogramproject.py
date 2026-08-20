
def show(balance):
    print(f"Your balance is ₹ {balance:.3f}")
          
    
def deposit():
    amount = float(input("Enter amount to be deposited : "))
    if amount < 0:
        print("Invalid Deposit")
        return 0
    else:
        return amount 

def withdraw(balance):
    amount = float(input("Enter money to be withdrawn: "))
    if amount > balance :
        print("You don't have that much money")
        return 0
    if amount < 0:
        print("Invalid Withdrawal")
        return 0
    else:
        return amount


def main():

    running = True
    balance = 0

    while running:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit ")

        choice = int(input("\nEnter your choice (1-4): "))

        if choice == 1:
            show(balance)

        elif choice == 2:
            balance = balance + deposit()

        elif choice == 3:
            balance =  balance - withdraw(balance)
        
        elif choice == 4:
            running = False

        elif choice not in (1,2,3,4):
            print("\nEnter Valid Input")

    print("Thank you ! Have a nice day. ")

if __name__=='__main__':
    main()