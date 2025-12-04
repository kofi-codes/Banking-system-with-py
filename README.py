# Banking-system-with-py
def showbalance(balance): 
  print(f"Your balance is Ghc{balance:.2f}.") 
def deposit(): 
  amount = float(input("Enter amount to be deposited: ")) 
  if amount < balance: 
    print("Number cannot be negative")      return 0 
  else: 
    return amount 
def withdraw(balance): 
    amount = float(input("Enter amount to be withdrawn: ")) 
  if balance < amount:       
    print("Insufficient funds") 
  else: 
    return amount 
def main():
  balance = 0 
  is_running = True 
  print("1.Check Balance") 
  print("2.Deposit") 
  print("3.Withdraw") 
  print("4.Exit") 
  while is_running: 
     choice = input("Enter your choice: ") 
    if choice == "1": 
       showbalance(balance) 
   elif choice == "2": 
       balance += deposit() 
   elif choice == "3": 
       balance -= withdraw(balance) 
   elif choice == "4": 
       is_running = False 
   else: 
       print("Invalid choice")
  
print("Have a nice a day")
