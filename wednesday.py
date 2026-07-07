#Real Time Project Example
#Employee Bonus
employee_name = input("Enter Employee Name:")
salary=float(input("Enter Salary:"))
if salary>=50000:
    bonus=salary*10/100
    print("Bonus=",bonus)

#ATM Withdrawal
balance=5000
withdraw=float(input("Enter Amount: "))
if withdraw<=balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")

#Login system
username = input("Enter Username: ")
password = input("Enter Password: ")
if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")  

#Employee bonus calculator
salary = float(input("Enter Salary: "))
if salary>=50000:
    bonus = salary*10/100
    print("Bonus=", bonus)
else:
    print("No Bonus") 

#Student pass or fail
marks = float(input("Enter Marks: "))
if marks >= 35:
    print("pass")
else:
    print("Fail")

#Driving License
age=int(input("Enter Age: "))
if age>=18:
    print("Eligible for Driving License")
else:
    print("Not Eligible")

#Electricity Bill Discount
bill = float(input("Enter Bill Amount: "))
if bill >= 5000:
    discount = bill*10/100
    final_bill = bill - discount
    print("Final Bill=",final_bill)
else:
    print("No Discount")                 