import threading
import time
class BankAccount:
    def __init__(self):
        self.balance=5000
        self.transactions=[]
        self.condition = threading.Condition()
       #Deposit Method
    def deposit(self,amount):
        with self.condition:
            print(f"\nDepositing ₹{amount}....")
            time.sleep(2)
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"Deposit Successful.")
            print(f"Available balance : ₹{self.balance}")

            #Notify waiting threads
            self.condition.notify_all()

    #Withdraw Method
    def withdraw(self,amount):
        with self.condition:
            while self.balance < amount:
                print(f"\nInsufficient Balance !")
                print(f"Need ₹{amount}, Available ₹{self.balance}")
                print("Waiting For deposit....\n")

                self.condition.wait()
            print(f"\nWithdrawing ₹{amount}....")
            time.sleep(2)

            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print("Withdrawal Successful.")
            print(f"Available Balance : ₹{self.balance}")

    #Mini Statement
    def mini_statement(self):
         with self.condition:
            print("\n--------MINI STATEMENT---------")
            if len(self.transactions) ==0:
                print("No Transactions")
            else:
                 for t in self.transactions:
                    print(t)
            print("----------------------")
            print("Curent Balance :",self.balance)
account =BankAccount()
#Threads
t1=threading.Thread(target=account.withdraw, args=(10000,))
t2=threading.Thread(target=account.deposit, args=(7000,))
t3=threading.Thread(target=account.mini_statement)
t1.start()

time.sleep(3)
t2.start()
t1.join()
t2.join()
t3.start()
t3.join()