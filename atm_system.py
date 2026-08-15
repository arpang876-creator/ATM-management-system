with open("balance.txt","r") as f:
  balance = int(f.read())

with open("pin.txt","r") as f:
    pin =  int(f.read())
    
name = ""
age = 0
account_no = 0
branch = ""

def register_detail():
    global name,age,account_no,branch
    name = input("Enter Account holder name")
    age = int(input("Enter age"))
    account_no = int(input("Enter account no:"))
    branch = input("Enter city of branch located in")

    

def deposit():
    global balance
    deposit_amount = int(input("Enter Deposit amount"))
    if deposit_amount > 0:
       balance += deposit_amount
       with open("balance.txt","w") as f:
         f.write(str(balance))
       with open("transactions.txt","a") as g:
         g.write(f"\nDeposit {deposit_amount}\n")
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
        with open("transactions.txt","a") as g:
            g.write(f"Withdraw {withdraw_amount}\n")
        print("Withdraw amount ",withdraw_amount)
        print("Current balance ",balance)
    elif withdraw_amount > balance:
        print("Insufficient balance.")
                 
    else:
        print("Amount cannot be negative")
      
    
def check_balance():
    print("Balance:",balance)


def transaction():
    global pin
    password = int(input("Enter the password"))
    if password == pin:
        print("=" *20)
        print("TRANSACTION HISTORY")
        print("=" *20)
        with open("transactions.txt","r") as f:
            data = f.readlines()
            for i in data:
                print(i.strip())
        print("="  *20)
    else:
        print("Invalid password,please try again.")


def pin_change():
    global pin
    old_pass = int(input("Enter your old pin"))

    if old_pass == pin:
        new_pass = int(input("Enter your new pin"))
        with open("pin.txt","w") as f:
            f.write(str(new_pass))
        pin = new_pass
        print("PIN changed successfully")
    else:
        print("Invalid old PIN")

def account_detail():
    global balance

    print("=" *20)
    print(" ACCOUNT DETAIL")
    print("=" *20)
    print("Name: ",name)
    print("Age: ",age)
    print("Account No: ",account_no)
    print("Branch: ",branch)
    print("Balance: ",balance)
    print("=" *20)

pin_attempt = 0
attempt = 0 

while pin_attempt < 5:
    
    try:
      print("=" *20)
      print("        ATM")
      print("=" *20)
      password = int(input("Enter your Pin"))

      if password == pin:
          print("Login Successful!")
          while True:
              print("=" *20)
              print("     MAIN MENU")
              print("=" *20)
              print("1.Register")
              print("2.Deposit")
              print("3.Withdraw")
              print("4.Check balance")
              print("5.transactions")
              print("6.Pin change")
              print("7.Account detail")
              print("8.Exit")
              print("=" *20)

              try:
                  choice = int(input("Enter your choice"))
                  if choice == 1:
                      attempt = 0
                      register_detail()
                  elif choice == 2:
                      attempt = 0
                      deposit()
                  elif choice == 3:
                      attempt = 0
                      withdraw()
                  elif choice == 4:
                      attempt = 0
                      check_balance()
                  elif choice == 5:
                      attempt = 0
                      transaction()
                  elif choice == 6:
                      attempt = 0
                      pin_change()
                  elif choice == 7:
                    attempt = 0
                    account_detail()
                  elif choice == 8:
                    attempt = 0
                    print("Have a great day!")
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
            print("You are blocked. We request you  to contact the bank")
            break
        

     


    




