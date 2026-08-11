with open("balance.txt","r") as f:
  balance = int(f.read())

def deposit():
    global balance
    deposit_amount = int(input("Enter Deposit amount"))
    if deposit_amount > 0:
       balance += deposit_amount
       with open("balance.txt","w") as f:
         f.write(str(balance))
       print("deposit amount ",deposit_amount)
       print("Current balance ",balance)
    else:
       print("Amount cannot be negative")
      

def withdraw():
    global balance
    withdraw_amount = int(input("Enter Withdraw amount"))
    if withdraw_amount > 0 : 
        balance -= withdraw_amount
        with open("balance.txt", "w") as f:
          f.write(str(balance))
        print("Withdraw amount ",withdraw_amount)
        print("Current balance ",balance)
                 
    else:
        print("Amount cannot be negative")
      
    


def check_balance():
    print("Balance:",balance)

pin_attempt = 0
attempt = 0

while pin_attempt < 5:
    
    try:
     
      password = int(input("Enter your Pin"))

      if password == 7575:
          while True:
              print("=" * 20)
              print("     ATM Machine")
              print("=" * 20)
              print("1.Deposit")
              print("2.Withdraw")
              print("3.Check balance")
              print("4.Exit")

              try:
                  choice = int(input("Enter your choice"))

                  if choice == 1:
                      deposit()
                  elif choice == 2:
                      withdraw()
                  elif choice == 3:
                      check_balance()
                  elif choice == 4:
                      print("Have a nice day")
                      break
                  else:
                      attempt += 1
                      print("Attempt left:", 3-attempt)

                  if attempt == 3:
                      print("Too many invalid inputs, Account blocked")
                      break

              except ValueError:
                  attempt += 1
                  print("Invalid input")
                  print("Attempt left:", 3-attempt)

                  if attempt == 3:
                      print("Your account has been blocked")
                      break
                  break
      else:
          pin_attempt += 1
          print("Invalid pin")
          print("Attempt left", 5-pin_attempt)

          if pin_attempt == 5:
              print("Your Account has been freezed")
              break
              

    except ValueError:
        pin_attempt += 1
        print("Invalid input")
        print("Attempt left:", 5-pin_attempt)

        if pin_attempt == 5:
            print("You are blocked. We request you visit the bank")
            break
        

     


    




