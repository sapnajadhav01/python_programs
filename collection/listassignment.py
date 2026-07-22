#1] Declare Array variable
arr=[]
print(arr)

#2] Initialize integer array with 5 values
arr=[10,20,30,40,50]
print(arr)

#3] Create Empty Integer Array with size 5
arr=[0]*5
print(arr)

#4] Display Length of following array
arr=[3,7,8,2,5,6,4]
print(len(arr))

#5]Display first Element of array
arr=[3,7,8,2,5,6,4]
print(arr[0])

#6]Display last Element of array
arr=[3,7,8,2,5,6,4]
last_element=arr[-1]
print(last_element)

#7]Display sum of first and last elemnts of array
arr=[3,7,8,2,5,6,4]
first_element=arr[0]
last_element=arr[-1]
sum=first_element+last_element
print("Sum of first and last element=",sum)

#8]Check the first element of array is even or not:
arr = [3, 7, 8, 2, 5, 6, 4]
first=arr[0]
if first %2==0:
    print("Even")
else:
    print("Not Even")

#9]Print Multiplication table for last element in the array:
arr = [3, 7, 8, 2, 5, 6, 4]
last_element=arr[-1]
for i in range(1,11):
    print(last_element,"x",i,"=",last_element*i)

#10]Display the middle element of following array of odd length:
arr = [3, 7, 8, 2, 5, 6, 4]  
middle_index=(len(arr)-1)//2
middle_element=arr[middle_index]
print("Middle Element=",middle_element) 

#2] type
arr = [3, 7, 8, 2, 5, 6, 4] 
middle_element=arr[3]
print("Middle Element=",middle_element)

#11]Display sum of 2 middle elements in the given even array of elements:
arr = [3, 7, 8, 2, 9, 5, 6, 4]
middle_index1=(len(arr))//2-1
middle_element1=arr[middle_index1]
middle_index2=(len(arr))//2
middle_element2=arr[middle_index2]
total=middle_element1+middle_element2
print("sum of 2 middle elements=",total)

#12]Display all elements in the array:
arr = [3, 7, 8, 2, 5, 6, 4]
print(arr[ : : ])

#13]Display array elements in reverse order:
arr = [3, 7, 8, 2, 5, 6, 4]
reverse_order=(arr[-1:-8:-1])
print("Array Elements in reverse order= ",reverse_order)

#14]Find the sum of array elements:
arr = [3, 7, 8, 2, 5, 6, 4]
total=0
for i in arr:
    total=total+i
print(total)

#15]Display only even numbers in the given array:
arr = [3, 7, 8, 2, 5, 6, 4]
for i in arr:
    if i%2==0:
        print(i)

#16]Count odd numbers in the given array:
arr =[3, 7, 8, 2, 5, 6, 4] 
count=0
for i in arr:
    if i %2!=0:
        count=count+1
print("count odd numbers=",count)

#17]Display Sum of Even elements in the given array:
arr = [3, 7, 8, 2, 5, 6, 4]
total=0
for i in arr:
    if i%2==0:
        total=total+i
print("Sum of Even element=",total)        
                    
#18]Display elements using for-each loop:
arr = [3, 7, 8, 2, 5, 6, 4]
for i in arr:
    print(i)

#19]Display sum of elements using for-each loop:
arr = [3, 7, 8, 2, 5, 6, 4]
total=0
for i in arr:
    total=total+i
print(total)  







    
       