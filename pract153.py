balance = 70000

def deposit():
    global balance
    deposit = int(input("Enter Deposit amount"))
    balance += deposit
    print(deposit)

def withdraw():
    global balance
    withdraw =int(input("Enter Withdraw amount"))
    balance -= withdraw
    print(withdraw)


def check_balance():
    print("Balance:",balance)

try:
       
  while True:

        
    print("=" *20)
    print("     ATM Machine")
    print("=" *20)

    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    print("4.Exit")


        
    choice = int(input("Enter your choice"))
    try:
          if choice == 1:
            deposit()
          elif choice == 2:
            withdraw()
          elif choice == 3:
            check_balance()
          elif choice == 4:
            print("Have a nice day")
            break
    except:
           print("Invalid input")

except:
    print("Invalid choice")


