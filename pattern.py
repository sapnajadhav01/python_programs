#1)
for i in range(5):
    for j in range(5,0,-1):
      print(j, end="")
    print()  

#2)
for i in range(5):
   for j in range(5):
      print(chr(65+i),end="")
   print()   

#3)
for i in range(65 , 71):
   for j in range(65,71):
      print(chr(j),end="")
   print()  

#4)
for i in range(1,6):
   for j in range(1,i+1):
      print("*",end="")
   print()   

#5)
for i in range(5,0,-1):
   for j in range(i):
      print("*",end="")
   print() 

#6)
for i in range(5,0,1):
   for j in range(5+i):
      print(" " * spaces+"*" * i)
   print()  

#7)
for i in range(6):
   for j in range(5):
      print(chr(70-i),end="")
   print()  
   
      