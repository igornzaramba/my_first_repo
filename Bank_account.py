import os
import uuid

class BankAccount(object):
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = str(uuid.uuid4())
        self.filename = str(self.accountNumber)+"_"+self.accountType+"_"+self.name+".txt"
        with open(self.filename, 'w') as f:
            f.write("Account created\n")

    def deposit(self, amount):
        self.balance += amount
        with open(self.filename, 'a') as f:
            f.write(f"Deposited {amount}. New balance: {self.balance}\n")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            with open(self.filename, 'a') as f:
                f.write(f"Withdrew {amount}. New balance: {self.balance}\n")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    def get_holder_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        with open(self.filename, 'r') as f:
            return f.read()
        
#To improve the code, I could implement a fonction that enable to manage multiple accounts 

def main():
    # Test the code !
    print("For testing puposes")
    account1 = BankAccount('Robo Garden', "Checking")
    


    
    while True:
        print("\n1. Deposit Money")
        print("2. Withdrawing Money")
        print("3. Checking balance")
        print("4. Getting account type")
        print("5. Getting account number")
        print("6. Getting account holder name")
        print("7. View transaction history")
        print("8. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '1':
            try:
                deposit = float(input("Enter the deposit amount: "))
                account1.deposit(deposit)
            except ValueError:
                print("Invalid input. Please enter a valid deposit amount.")

        elif choice == '2':
            try:
                withdraw = float(input("Enterthe withdraw amount: "))
                account1.withdraw(withdraw)
            except ValueError:
                print("Invalid input. Please enter a valid withdraw amount.")

        elif choice == '3':
            print("The account balance is: ", account1.get_balance())

        elif choice == '4':
            print("The account type is :", account1.get_account_type())

        elif choice == '5':
            print("The account number is:", account1.get_account_number())

        elif choice == '6':
            print("The account holder is:",account1.get_holder_name())

        elif choice == '7':
            print(account1.get_transaction_history())

        elif choice == '8':
            print("Exiting the account. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 8")

#To improve the code, I could implement a fonction that to add and manage multiples accounts
main()
