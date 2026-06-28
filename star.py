##square pattern
n=int(input("Enter a number:"))
for i in range(n):
    print("*" *n)

#2)
n=int(input("Enter a number:"))
for i in range(n):
    print((str(n)+" ")*n)  

#3)
n=int(input("Enter a number of rows:"))
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()   

#4)
n=int(input("Enter a number of rows: "))
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="",)
    print() 

#5)
for i in range(1,6):
    for k in range(1,6-i):
        print(" ",end="")
    for j in range(1,i+1):                  
        print("*",end="")
    print()    

#6)
for i in range(5,0,-1):
    for k in range(5,0+i):
        print("",end="")
    for j in range(i):
        print("*",end="")
    print() 

#7)
for i in range(1,6,-1):
    for k in range(1,6-i,0+i):
        print("",end="")
    for j in range(i):
        print("*",end="")
    print()                  

#8)
for i in range(1,6):
    print("*" *i)
for i in range(4,0,-1):
    print("*"*i)    

#9)
for i in range(6):
    for j in range(5):    
        print(chr(70-i),end="")
    print()  

#10)
for i in range(1,6):
    for j in range(1,6):
        if j>=i:
            print("*",end="")
        else:
            print(" ",end="")      
    print()

#11)
for i in range(5,0,-1):
    for k in range(5,0+i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()  

#12)
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()  

#13)
for i in range(5):
    for j in range(1,6):
        print(j,end="")
    print()

#14)
for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print() 

#15)
for i in range(5):
    for j in range(1,6):
        print("*",end="")
    print()  

#16)
for i in range(5):
    for j in range(5,0,-1):
        print(j,end="")
    print()

#17)
for i in range(5,0,-1):
    for j in range(1,6):
        print(i,end="")
    print()    

#18)
for i in range(5):
    for j in range(5):
        if j%2==0:
          print("1",end="")
        else:
            print("0",end="")
    print()

#19)
for i in range(5):
    for j in range(5):
        if i % 2==1:
            print("0",end="")
        else:
            print("1",end="")
    print()  

#20)
for i in range(5):
    for j in range(5):
        print(chr(65+i),end="") 
    print()

#21)
for i in range(5):
    for j in range(5):
        print(chr(65+j),end="")
    print()

#22)
for i in range(5):
    for j in range(5):
        print(chr(69-i),end="")
    print() 

#23)
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(chr(36),end="")
        else:
            print(chr(35),end="")
    print()           

#24)
for i in range(5):
    for j in range(5):
        print(chr(69-j),end="")
    print()  

#25)
for i in range(5):
    for j in range(5):
        if j%2==0 :
            print(chr(36),end="")
        else:
            print(chr(35),end="")
    print() 

#26)
for i in range(5):
    for j in range(1,6):
        num=(i+j-1)%9+1
        print(num,end="")
    print()          