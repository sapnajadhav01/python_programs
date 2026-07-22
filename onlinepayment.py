#Online Payment
from abc import ABC,abstractmethod
class Payment(ABC): #interface
    @abstractmethod
    def pay(self,amount):
        pass

#1] Credit Card Payment      
class CreditCardPayment(Payment):
    def __init__(self,card_number,cvv,expiry_date):
        self.card_number=card_number
        self.cvv=cvv
        self.expiry_date=expiry_date

    def pay(self,amount):
        print("Card Number:",self.card_number)
        print("CVV:",self.cvv)
        print("Expiry date:",self.expiry_date)
        print("Amount:",amount)
        print("Credit Card Payment Successful")

#2] DebitCardPayment
class DebitCardPayment(Payment):
    def __init__(self,card_number,atm_pin,bank_name):
         self.card_number=card_number
         self.atm_pin=atm_pin
         self.bank_name=bank_name

    def pay(self,amount):
        print("Card Number:",self.card_number)
        print("ATM PIN:",self.atm_pin)
        print("Bank Name:",self.bank_name)
        print("Amount:",amount)
        print("Debit Card Payment Successful") 

#3] UPIPayment
class UPIPayment(Payment):
    def __init__(self,UPI_ID,UPI_PIN):
        self.UPI_ID=UPI_ID
        self.UPI_PIN=UPI_PIN

    def pay(self,amount):
        print("UPI ID:",self.UPI_ID)
        print("UPI_PIN:",self.UPI_PIN)
        print("Amount:",amount)
        print("UPI Payment Successful")

#4] PayPal Payment
class PayPalPayment(Payment):
    def __init__(self,Email_ID,Password):
        self.Email_ID=Email_ID
        self.Password=Password  

    def pay(self,amount):
        print("Email ID:",self.Email_ID)
        print("Password:",self.Password)
        print("Amount:",amount)
        print("PayPal Payment Successful")

#5] NetBanking Payment
class NetBankingPayment(Payment):
    def __init__(self,Bank_name,User_ID,Password,Transaction_ID):
        self.Bank_name=Bank_name
        self.User_ID=User_ID
        self.Password=Password
        self.Transaction_ID=Transaction_ID

    def pay(self,amount):
        print("Bank Name:",self.Bank_name)
        print("User ID:",self.User_ID)
        print("Password:",self.Password)
        print("Transaction ID/OTP:",self.Transaction_ID)
        print("Amount:",amount)
        print("NetBanking Payment Successful")

print("\n=========ONLINE PAYMENT SYSTEM==========")
print("1.Credit Card")
print("2.Debit Card")
print("3.UPI")
print("4.PayPal")
print("5.NetBanking")

choice=int(input("Enter Your Choice: "))

if choice==1:
   print("==============Credit Card Payment==================")
   credit=CreditCardPayment("1234656767676","123","12/28")
   credit.pay(5000)

if choice==2:      
    print("==============Debiit Card Payment==================")
    debit=DebitCardPayment("1236573475674","1996","SBI")
    debit.pay(2000)

if choice==3:    
    print("==============UPI Payment==================")
    upi=UPIPayment("2535263136137","2005")
    upi.pay(500)

if choice==4:    
    print("==============PayPal Payment==================")
    pay=PayPalPayment("sapnajadhav@gmail.com","9356")
    pay.pay(1000)

if choice==5:    
    print("==============NetBanking Payment==================")
    netbanking=NetBankingPayment("SBI","1234565432","5445","982991828247")
    netbanking.pay(2000)

            


