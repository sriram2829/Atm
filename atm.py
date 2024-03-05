print("WELCOME TO THE CANARA BANK::")
print("select an option for you need")
print("1.Balance")
print("2.Withdraw")
print("3.Deposit")
print("4.exit")

bal=int(input("Enter the balance: "))
option=int(input("Enter the transaction: "))
if(option==1):
    print("balance=",bal)
elif(option==2):
    withdraw=int(input("Enter the withdraw: "))
    if(withdraw<bal):
        total=bal-withdraw
        print("Balance amount in your account=",total)
    else:
        print("insufficient balance")
elif(option==3):
    deposit=int(input("enter the deposit: "))
    totalamount=bal+deposit
    print("balance in your account:",totalamount)

elif(option==4):
    exit()
else:
    print("transcation wrong")
