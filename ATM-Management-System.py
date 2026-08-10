balance = 70000

def deposit():
    global balance
    deposit_amount = int(input("Enter Deposit amount"))
    if deposit_amount > 0:
       balance += deposit_amount
       print(deposit_amount)
    else: 
       print("Amount cannot be negative")
      

def withdraw():
    global balance
    withdraw_amount = int(input("Enter Withdraw amount"))
    if withdraw_amount > 0 : 
        balance -= withdraw_amount
        print(withdraw_amount)
                 
    else:
        print("Amount cannot be negative")
      
    


def check_balance():
    print("Balance:",balance)


class Attempt:
  """Track invalid PIN/menu attempts and determine when access is blocked."""

  def __init__(self, maximum=3):
    self.maximum = maximum
    self.count = 0

  def record(self):
    self.count += 1

  def remaining(self):
    return max(0, self.maximum - self.count)

  def is_blocked(self):
    return self.count >= self.maximum

pin = 0
password =int(input("Enter your Pin"))
if password == 7575:

  attempt = Attempt()
  while True:

        
    print("=" *20)
    print("     ATM Machine")
    print("=" *20)

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
        attempt.record()
      print("Attempt left:", attempt.remaining())

      if attempt.is_blocked():
        print("Too many invalid inputs, Account blocked")
        break

    except ValueError:
     attempt.record()
    print("Invalid input")
    print("Attempt left:", attempt.remaining())

    if attempt.is_blocked():
      print("Your account is blocked")
      break

else:
  pin += 1
  print("Invalid pin")
  print("Attempt left",5-pin)

  if pin == 5:
    print("Your Account is freezed")






