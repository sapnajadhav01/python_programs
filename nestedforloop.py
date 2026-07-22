#1]
for i in range(4):
    for j in range(1,6):
        print(j,end="")
    print()

#2]
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print()    

#3]
for i in range(5):
    for j in range(1,6):
        print("*",end=" ")
    print()    
#4]
for i in range(5):
    for j in range(5,0,-1):
        print(j,end="")
    print()    

#5]
for i in range(5,0,-1):
    for j in range(1,6):
        print(i,end=" ")
    print()    

#6]
for i in range(5):
    for j in range(5):
        if j%2==0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print() 
#character pattern
#7]
for i in range(5):
    for j in range(5):
        print(chr(65+i),end=" ")
    print()

#8]               
for i in range(5):
    for j in range(5):
        print(chr(65+j),end=" ")
    print()

#9] 
for i in range(5):
    for j in range(5):
       print(chr(69-i),end=" ")
    print()

#10]
for i in range(5):
    for j in range(5):
        print(chr(69-j),end=" ")
    print()  

#Basic patterns with conditions
#11]
for i in range(5):
    for j in range(5):
        if i%2==0:
            print(chr(36),end=" ")
        else:
            print(chr(35),end=" ")
    print()            

#12]
for i in range(5):
    for j in range(5):
        if j%2==0:
            print(chr(36),end=" ")
        else:
            print(chr(35),end=" ")
    print() 

#13]
rows=5
cols=5
for i in range(1,rows+1):
    for j in range(1,cols+1):
        if i%2==1:
            print( rows-i+1,end=" ")
        else:
            print(rows-j+1,end=" ")
    print()    


#14]
for i in range(1,6):
    for j in range(1,i+1):
            print(j,end=" ")
    print() 
#15]
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()     

#16]
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()       
#17]
for i in range(1,6):
    for j in range(i,6):
        print(j,end=" ")
    print()    
#18]
for i in range(1,6):
    for j in range(5,5-i,-1):
        print(j, end=" ")
    print()  

#19]
for i in range(5,0,-1):
    for j  in range(i,6):
        print(j,end=" ")
    print()  

#20]
for i in range(5,0,-1):
    for j in range(i,6):
        print(i,end="")
    print()                
#21]
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end="")
    print()                


                      