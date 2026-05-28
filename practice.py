#WAP to check the number is not zero
num=int(input("Enter a number="))
if(num!=0):
    print("num is Not zero")
else:
    print("num is zero")  

#WAP to check two numbers equal or not
n1=int(input("Enter First number="))
n2=int(input("Enter Second number"))
if(n1==n2):
    print("Equal")
else:
    print("Not Equal") 

#WAP to check first number is greater than second number
n1=int(input("Enter a first number= "))
n2=int(input("Enter second number="))
if(n1>n2):
    print("First is greater")
else:
    print("first is not greater") 

#WAP to check sum of two numbers equals to 10
a=int(input("Enter first number="))
b=int(input("enter second number="))
if(a+b==10):
    print("equals to 10")
else:
    print("Not equals to 10")

#WAP to check the first two numbers multiplication quals third number
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if(a*b==c):
    print("Multiplication of first two numbers equals to third num")
else:
    print("multiplication of two numbers not equals to third num")

#WAP to check average of four numbers greater than 60
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
d=int(input("Enter fourth number="))
avg=(a+b+c+d)/4
print ("average=",avg)
if avg>60:
    print("greater than 60")
else:
    print("not greater than 60")    

#WAP to check the number is divisible by 7
num=int(input("Enter a number="))
if(num%7==0):
    print("number is divisible by 7")
else:
    print("number is not divisible by 7")

#WAP to check the num is not divisible by 100
num=int(input("Enter a number="))
if(num%100!=0):
    print("Not divisible")
else:
    print("divisible")    

#WAP to check the square of first num equals to cube of the second num
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if(a**2==b**3):
    print("equals")
else:
    print("not equals")

#WAP to check the last digit of num is 5
num=int(input("Enter first number="))
if(num%10==5):
    print("num is 5")
else:
    print("num is not 5")

#WAP to check the last digit of given three nums is equal to 10
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if((a%10)+(b%10)+(c%10)==10):
    print("sum of last digit equals 10")
else:
    print("sum of last digit not equals 10")    

#WAP to check the sum of first 2 nums last digits equals to square of the 3rd number
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if((a%10)+(b%10)==(c**2)):
    print("Equals")
else:
    print("Not equals")

#WAP to check the first and second numbers are equal when we remove last digit of second num
a=int(input("Enter first number="))
b=int(input("Enter second number="))
if(a==b//10):
    print("equal after remove last digit")
else:
    print("not equal") 

#WAP to check the last digit of given number divisible by 3
a=int(input("Enter a number:"))
if((a%10)%3==0):
    print("Divisible")
else:
    print("Not divisible")
        
#WAP to check the sum of first 2 numbers equals to last digit of 3rd number
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if(a+b==(c%10)):
    print("equals")
else:
    print("Not equals")    

#WAP to check the average of 3 numbers equals to first number
a=int(input("Enter first number="))
b=int(input("Enter second number="))
c=int(input("Enter third number="))
if((a+b+c)/3==a):
    print("equals")
else:
    print("Not equals")

#WAP to check the square of last digit is greater than 10
a=int(input("Enter a number="))
if((a%10)**2>10):
    print("greater")
else:
    print("not greater")

#WAP to check the square of last digit of given number is divisible by 3
a=int(input("Enter a number="))
if((a%10)**2%3==0):
    print("last digit divisible by 3")
else:
    print("last digit Not divisible by 3")    