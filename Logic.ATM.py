def atm():  # ATM program
    correct_pin = "42069"  # correct pin
    balance = 1000  # starting balance

    print("Welcome to T's ATM")  # welcome message
    attempts = 3  # number of attempts

    # Pin check loop
    while attempts > 0: # loop until pin is correct or attempts run out
        pin = input("Please enter your PIN: ") # user input for pin
        if pin == correct_pin: # pin is correct
            print("Access granted to the account") # access granted message

            while True: # ATM menu loop
                print ("\nATM Menu:") # display menu
                print("(1) Check Balance") # check balance option
                print("(2) Deposit Money") # deposit money option
                print("(3) Withdraw") # withdraw money option
                print("(4) Exit") # exit option

                choice = input("Choose between 1-4: ") # user input for choice

                if choice == "1": # check balance option
                    print(f"Your balance is: ${balance}") # display balance
                elif choice == "2": # deposit money option
                    amount = float(input("Enter amount of deposit:")) # user input for deposit amount
                    balance += amount # update balance
                    print(f"${amount} deposited. New balance is ${balance}") # display new balance
                elif choice == "3": # withdraw money option
                    amount = float(input("Enter amount of withdrawal:")) # user input for withdrawal amount
                    if amount > balance: # check if withdrawal amount is greater than balance
                        print("You are too broke to take out that much money!") # display error message
                    else: # withdraw money
                        balance -= amount # update balance
                        print(f"{amount} was taken out of your account. Your new balance is ${balance}") # display new balance
                elif choice == "4": # exit option
                    print("Thank you for stopping by to this branch of T's atm. Have a good one!") # exit message
                    break # exit the ATM menu loop
                else: # invalid choice
                    print("DUDE, YOU HAD OPTIONS 1,2,3, OR 4.... TRY AGAIN")  # display error message
            
            break # exit the pin check loop
        
        
        else: # pin is incorrect
            attempts -= 1 # decrement attempts
            print(f"HAHA! INCORRECT! Attempts remaining {attempts}") # display attempts remaining

atm()  # <- This calls the function
