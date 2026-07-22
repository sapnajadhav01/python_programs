#print number 2,4,6,8,10
i=2
for i in range(2,10,2):
    print(i)

# range
i=15
for i in range(15,-1,-3):
    print(i)

#print numbers 10,20,30,40,50
i=10
for i in range(10,55,10):
    print(i)

#print numbers 100,80,60,40,20
i=100
for i in range(100,10,-20):
    print(chr(i))

#print lower case alphabets a to z
i=97
for i in range(97,123):
    print(chr(i))

#print upper case alphabets in reverse order Z to A
i=90
for i in range(90,66,-1):
    print(chr(i))

#program to print ascii values from A-Z
i=65
for i in range(ord('A'),ord('Z')):
    print(chr(i),"=",i)

#program to print ascii values of 0-9
i=48
for i in range(48,58):
    print(chr(i),"=",i)

# program to display ascii character set
# WAP to print square values for numbers 1 to 5
i=1
for i in range(1,6):
    print("Square","=",i*i)

# WAP to print cube values for numbers 1 to 5
i=1
for i in range(1,6):
    print("cube","=",i*i*i)

# WAP to print the numbers divisible by 7 between 20 and 60 
i=20
for i in range(20, 61):
    if i%7==0:
        print(i)

#WAP to print numbers divisible by 3 and not divisible by 5 between 10 to 50
i=10
for i in range(10,51):
    if i % 3 ==0 and i % 5 != 0:
        print(i)    

#WAP to print number divisible by 4 and not divisible by 100 from 100 to 300
i=100
for i in range(100,301):
    if i%4==0 and i%100!=0 :
        print(i)

#WAP to print numbers which are not divisible by 5 from 30 to 70
i=30
for i in range(30,71):
    if i%5 !=0:
        print(i)

#WAP to print even numbers from 1 to 30 which are not divisible by 5
i=1
for i in range(1,31):
    if i%2==0 and i%5!=0:
        print(i)

#WAP to display multiplication table
num=int(input("Enter a number="))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#WAP to display even number from 1 to 10
for i in range(1,11):
    if i%2==0:
        print(i)            
#Program to count factors of given number
num=int(input("Enter a number:"))
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
        print("Number of factor=",count)

#program to print factors of given numbers
num=int(input("Enter a number"))
for i in range(1,num+1):
    if num%i==0:      
        print(i)

#program to find the sum of factors of given number
num=int(input("Enter a number="))
sum=0
for i in range(1,num+1):
    if num%i==0:
        sum=sum+i
        print("Sum of factors=",sum)

