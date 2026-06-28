# 1)WAP to print even numbers between 100 to 200
i=100
while(i<=200):
    if(i%2==0):
      print(i)
    i=i+1

#2)WAPP to print the multipliction table of 5
num=int(input("Enter a number="))
i=1
while(i<=10):
   print(num,"x",i,"=",num*i)
   i += 1

#3)WAP to print numbers from 1 to 10
i=1
while(i<=10):
   print(i)
   i=i+1   
    
#4)WAP to print sum first n natural number
num=int(input("Enter a number:"))
total=0
i=1
while(i<=num):
   total=total+i
   i=i+1
   print("Sum of first",num,"natural numbers is",total)  

#5)WAP to print palindrome or not                    h 
num=int(input("Enter a number:"))
temp=num
rev=0
while num>0:
   remainder=num%10
   rev=rev*10+remainder
   num=num//10
if temp==rev:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome") 

#6) palindrome program
num = 153
temp = num
rev = 0
while num>0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if temp == rev:
    print("The ",temp,"is a palindrome ")
else:
    print("The ",temp," is not a palindrome") 

#7)WAP to check the number is armstrong or not
num = int(input("Enter a Number: "))
temp = num
digits = len(str(num))
total = 0

while num > 0:
    rem = num % 10
    total = total + rem ** digits
    num = num // 10

if temp == total:
    print("The", temp, "is an Armstrong number")
else:
    print("The", temp, "is not an Armstrong number")

#8)Check the number is even or not untill user exits
while True:
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        print(num, "is an Even number")
    else:
        print(num, "is an Odd number")

    choice = input("Do you want to continue? (yes/no): ")

    if choice.lower() == "no":
        print("Program exited.")
        break

#9)check the given 3 digit number or not
num=153
temp=num
total=0
while num>0:
    rem=num%10
    total=total+rem**3
    num=num//10
if temp==total:
    print(temp,"is armstrong")
else:
    print(temp,"is not armstrong")   

#WAP to check the number is armstrong or not
#num=1634
num=1634
temp=num
total=0
digits=(len(str))     
while num>0:
    rem=num%10
    total=total+digits**digits
    num//10
if temp==total:
    print(temp,"is armstrong number")
else:
    print(temp,"is not armstrong number")    
