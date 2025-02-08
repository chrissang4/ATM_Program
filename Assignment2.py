# ATM PROGRAM
# Initialize the user's balance with Ksh.1000
balance = 1000

while True:
    # Function displaying User's menu 
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    # Get the user's choice
    choice = input("Please enter a choice (1-4): ")
    # Get user's choice
    if choice == '1':
        # Option 1: Check Balance
        print(f"\nYour current balance is: Ksh.{balance}")
    
    elif choice == '2':
        # Option 2: Deposit Money
        deposit_amount = float(input("\nEnter amount to deposit: "))
        if deposit_amount > 0:
            balance += deposit_amount  
            print(f"\nDeposit of ksh{deposit_amount} was successful. New balance: is ksh {balance}")
        else:
            print("Invalid amount. Please enter a positive value.")
    
    elif choice == '3':
        # Option 3: Withdraw Money
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > 0:
            if withdraw_amount <= balance:
                balance -= withdraw_amount  
                print(f"Ksh.{withdraw_amount} has been withdrawn successfully. Your new balance is: Ksh.{balance}")
            else:
                print("You have Insufficient funds. Check your current balance and try again.")
        else:
            print("Invalid amount. Please enter a positive value.")
    
    elif choice == '4':
        # Option 4: Exiting the ATM program
        print("Thank you for using ATM services.")
        break  
    else:
        # Handle invalid menu choices
        print("Invalid choice. Please select a valid option (1-4).")