active = True


balance = 0.00
def menu():
    print("1. Check Balance\n 2. Withdraw\n 3. deposit 4.\n \
        Transaction History")

userinput = int(input)
if userinput == 1:
    print(f"Your current balance is: ${balance}")
    menu()

if userinput == 2: 
    print(f"Your current balance is: ${balance}")
    input("How much money would you like to withdraw: ")

if userinput == 3:
    print()

if userinput == 4:
    print()

def withdraw(): 








#while active == True:
#   print() 