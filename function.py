#Banking management
customers={
    1001:{
        "name":"Sapna",
        "account_type":"Savings",
        "balance":100000,
        "History":[]
    },
    1002:{
        "name":"Divya",
        "account_type":"Current",
        "balance":40000,
        "History":[]
    },
    1003:{
        "name":"Ashu",
        "account_type":"Savings",
        "balance":10000,
        "History":[]
    },

}
#Create Account
def create_account():
    acc_no=int(input("Enter Account Number: "))

    if acc_no in customers:
        print("Account Already exists!")
        return
    name=input("Enter Customer Name: ")
    account_type=input("Enter Account type (Saving/Current): ")
    balance=float(input("Enter Initial Balance: "))
    
    customers[acc_no] = {
        "name"        : name,
        "account_type": account_type,
        "balance"     : balance,
        "History"     : ["Account created"]
    }
    print("\nAccount Created Successfully")
    print("-"*50)

#Diposit 
def deposit(acc_no,amount):
    if acc_no in customers:
       customers[acc_no]["balance"]+=amount
       customers[acc_no]["History"].append(f"Deposited {amount}")
       print("\n Deposit Successful")
       print("Deposit Amount :",amount)
       print("Current Balance:",customers[acc_no]["balance"])
       print("-"*50)

#Withdrow:
def withdraw(acc_no,amount):
    if acc_no in customers:
      if customers[acc_no]["balance"]>=amount:
        customers[acc_no]["balance"]-=amount
        customers[acc_no]["History"].append(f"withdraw {amount}")
        print("\nWithdraw Successfully")
        print(" Withdraw Amount :",amount)
        print("Current Balance  :",customers[acc_no]["balance"])
        print("-"*50)   

#Check balance:
def check_account(acc_no):
    if acc_no in customers:
        print("Account Found")
        print("Name         :",customers[acc_no]["name"])
        print("Account Type :",customers[acc_no]["account_type"])
        print("balance      :",customers[acc_no]["balance"])
        print("History      :",customers[acc_no]["History"])
    else:
        print("Account Not Found") 
        print("-"*50)  

#Fund Transfer:
def fund_transfer(sender_acc, receiver_acc, amount):
    if sender_acc in customers and receiver_acc in customers:
        if customers[sender_acc]["balance"] >= amount:
            customers[sender_acc]["balance"] -= amount
            customers[receiver_acc]["balance"] += amount
            customers[sender_acc]["History"].append(f"Trasferred {amount} to {receiver_acc}")
            customers[receiver_acc]["History"].append(f"Received {amount} from {sender_acc}")
            print("Fund Transfer Successful")
        else:
            print("Insufficient Balance")

    else:
        print("Invalid Account Number")  

#Search Customer:-
def search_customer(acc_no):
    if acc_no in customers:
        print("Customer Found")
        print("Name              :",customers[acc_no]["name"])
        print("Account Type      :", customers[acc_no]["account_type"])
        print("Balance           :",customers[acc_no]["balance"])
    else:
        print("Customer Not Found")            

#Update Customer:
def update_customer(acc_no):
    if acc_no in customers:
        customers[acc_no]["name"] = input("Enter New Name:  ")
        customers[acc_no]["account_type"] = input("Enter New Account Type: ")
        print("Customer Updated Successfully")
    else:
        print("Customer Not Found")

#Delete Account
def delete_account(acc_no):
    if acc_no in customers:
        del customers[acc_no]
        print("Account Deleted Successfully")
    else:
        print("Account Not Found")
        

#Transaction History
def transaction_History(acc_no):
    if acc_no in customers:
        print("\n Transaction History")
        for transaction in customers[acc_no]["History"]:
            print(transaction)
    else:
        print("Account not found")
        print("-"*50)   

def display_all_customers():
    print("Display All Customers")
    print("="*50)
    for cust_Id,details in customers.items():
        print("Customer ID   :",cust_Id)
        print("Name          :",details["name"])
        print("Account Type  :",details['account_type'])
        print("Balance       :",details['balance'])
        print("-"*50)

while True:
    print("\n=========BANK MANAGEMENT SYSTEM=========")
    print("1. Create Account")
    print("2. Deposite")
    print("3. withdraw")
    print("4. Check Balance")
    print("5. Fund Transfer")
    print("6. Search Customers")
    print("7. Update Customer")
    print("8. Delete Account")
    print("9. Transaction History")
    print("10. Display All Customers")
    print("11. Exit")

    choice =int(input("Enter Your choice: "))

    if choice == 1:
        create_account()

    elif choice == 2:
        acc = int(input("Enter Account number: "))
        amount = float(input("Enter Amount: "))
        deposit(acc,amount)   

    elif choice == 3:
        acc = int(input("Enter Account Number: "))
        amount = float(input("Enter Amount:"))
        withdraw(acc,amount)

    elif choice == 4:
        acc = int(input("Enter Account Number: "))
        check_account(acc)

    elif choice == 5:
        sender = int(input("Enter Sender Account Number: "))
        receiver = int(input("Enter Receiver Account Number: "))
        amount = float(input("Enter Amount: "))
        fund_transfer(sender, receiver, amount)

    elif choice == 6:
        acc = int(input("Enter Account Number: "))
        search_customer(acc)

    elif choice == 7:
        acc= int(input("Enter Account Number: "))
        update_customer(acc)

    elif choice == 8:
        acc= int(input("Enter Account Number:"))
        delete_account(acc)

    elif choice == 9:
        acc = int(input("Enter Account Number: "))
        transaction_History(acc)

    elif choice == 10:
        print("Display All Customers")
        for cust_id, details in customers.items():
            print(cust_id, details)

    elif choice == 11:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")



