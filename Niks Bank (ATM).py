#Niks Bank
print("Welcome To Niks Bank")
restart=('Y')
chances=3
balance = 2400000
while chances >= 0:
    pin = int(input("Please Enter Your Digit Pin: "))
    if pin == (1234):
        print("You May Proceed\n")
        while restart not in ('n', 'NO','no', 'N'):
            print("Please press 1 to check your balance\n")
            print("Please press 2 for withdrawl\n")
            print("Please press 3 to pay in\n")
            print("Please press 4 to return card\n")
            option = int(input("Choose any of the options to proceed:"))
            if option == 1:
                print("Your balance is Rupees",balance,'\n')
                restart = input("Would you like to go back?")
                if restart in ('n', 'NO','no', 'N'):
                    print("Thank You")
                    break
            elif option == 2:
                option2 = ('Y')
                withdrawl = float(input("Enter amount:"))
                if withdrawl in [100,200,600,800,1000]:
                    balance = balance - withdrawl
                    print("\n Your Balance is Rupees", balance)
                    restart = input("Would you like to go back?")
                    if restart in ('n', 'NO','no', 'N'):
                        print("Thank You \n Visit Again")
                        break
                elif withdrawl != [100,200,600,800,1000]:
                    print("Invalid amount,Please re-try\n")
                    restart = ('Y')
                elif withdrawl==1:
                    withdrawl = float(input("Please enter Desired amount"))

            elif option == 3:
                Pay_in = float(input("Enter Pay In Amount"))
                balance = balance + Pay_in
                print("\n Your balance is Rupees",balance)
                restart = input("Would you like to go back?")
                if restart in ('n', 'NO','no', 'N'):
                    print("Thank You \n Visit Again")
                    break

            elif option == 4:
                print("Please Wait & Collect Your Card.....!!!\n")
                print("Thank You For Visiting Niks Bank")
                break
            else:
                print("Please Enter Correct Number. \n")
                restart = ('Y')
    elif pin != ("1234"):
        print("Incorrect Password")
        chances = chances - 1
        if chances == 0:
            print("Sorry Please Visit Nearest Branch")
            break