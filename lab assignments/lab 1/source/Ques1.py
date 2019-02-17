#Initializing the variables
total = 0
choice = 0
deposit = 0
withdraw = 0
while int(choice) != 4:  #Iterating the loop by considering the choices of user
    print("Type 1 for Deposit **  Type 2 for Withdraw ** Type 3 to know your total ** Type 4 to exit")
    print("Please select the type of transaction from above options:")
    choice = input()
    if int(choice) == 1:
        print("Enter the amount to be deposited :")
        deposit = input()
        total += int(deposit)
    elif int(choice) == 2:
        print("Enter the amount to be withdrawed :")
        withdraw = input()
        total -= int(withdraw)

    elif int(choice) == 3:
        print("your total will be : %d" %(total))
    else:
        exit()