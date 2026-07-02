#Beginner level
#1]Create a tuple with 5 student names and print it
student=("Sapna","Bhavana","Manisha","Kalyani","Dipti")
print(student)

#2]Create a tuple of numbers and print the first and last element.
tup=(1,3,18,30,26,22)
print("first_element",tup[0])
print("last_element",tup[-1])

#3]Find the length of tuple.
tup=(1,3,18,30,26,22)
print("length of tuple",len(tup))

#4]Check whether a value exists in a tuple
tup=(1,3,2,16,17,15,21,23)
value=16
if value in tup:
    print("value is exist in tuple")
else:
    print("Value is not exist in Tuple")

#5]Count how many times an element appears in a tuple
tup=(1,3,18,30,26,22,1,18)
print("Element appear is",tup.count(18))

#6]Find the index of a given element in a tuple
tup=(1,3,18,30,26,22,1,18)
print(tup.index(18))

#7]Convert a list into a tuple
lst=[101,201,301,401,501]
tup=tuple(lst)
print("Tuple:",tup)

#8]concatenate two tuples
t1=(1,3,18,30,26,22,1,18)
t2=(101,201,301,401,501)
t3=t1+t2
print(t3)

#9]Repeat a tuple 3 times using * operator.
t1=(1,3,18,30,26,22,1,18)
t2=t1*3
print(t2)

#Intermediate level
#10]Find the maximum value in a tuple
even_nums=(10,20,30,40,50,100)
print("Maximum value Tuple:",max(even_nums))

#11]Find the minimum value in a tuple.
print("Minimum Value Tuple:",min(even_nums))

#12]Find the sum of all elemnts in a tuple
print("Total of tuple:",sum(even_nums))

#13]Find the average of tuple elements.
avg=(sum(even_nums)/len(even_nums))
print("Average:",avg)

#14]Reverse a tuple.
names=("Sapna","Sarvesh","Prachi","Krishna","Aaru")
reverse_tuple=names[::-1]
print("Original tuple:",names)
print("reverse tuple:",reverse_tuple)

#15]Sort tuple elements in ascending order
num=(88,2,44,53,65,21,1,3,99,54,100,5)
element=sorted(num)
print(element)

#16]Sort tuple elements in descending order
num=(88,2,44,53,65,21,1,3,99,54,100,5)
elements=sorted(num,reverse=True)
print(elements)

#17]Slice a tuple to get elements from index 2 to 5
num=(88,2,44,53,65,21,1,3,99,54,100,5)
print(num[2:5])

#18]Unpack tuple values into separate variables
t2=(10,20,30,40,50)
x1,x2,x3,x4,x5=t2
print(x1)
print(x2,x3,x4,x5)

#19]Swap two variables using tuple unpacking
t1=(10,20,30,40)
t2=(2,3,4,5)
t1,t2=t2,t1
print("t1=",t1)
print("t2=",t2)



#Tuple Loop Questions
#20]Print all elements of a tuple using a for loop
names=("Sapna","Sarvesh","Prachi","Krishna","Aaru")
for name in names:
    print(name)

#21]Print tuple elements with index values
names=("Sapna","Sarvesh","Prachi","Krishna","Aaru")
for i in range (len(names)):
    print(i,":",names[i])

#22]Count even numbers in a tuple
nums=(1,2,3,4,5,6,7,8,9,11,21,22,33,44)
count=0
for i in nums:
   if i%2==0:
       count=count+1
print("Even numbers in tuple:",count) 

#23]Count odd numbers in tuple
nums=(1,2,3,4,5,6,7,8,9,11,21,22,33,44)
count=0
for i in nums:
   if i%2!=0:
       count=count+1
print("Odd numbers in tuple:",count) 

#24]Print all positive numbers from a tuple
nums=(1,2,-5,-29,11,-44,21,22,33,44)
for i in nums:
    if i>0:
        print(i)

#25]Print all negative numbers from a tuple
nums=(1,2,-5,-29,11,-44,21,22,33,44)
for i in nums:
    if i<0:
        print(i)

#26]Find the second largest element in a tuple
tup=(10,21,9,18,2,3,17,1)
lst=list(tup)
print(lst)
ac=sorted(lst)
print(ac)
second_largest=ac[-2]
print("Second largest elemnt in tuple:",second_largest)


#27]Find the second smallest elements in a tuple
tup=(10,21,9,18,2,3,17,1)
print("Second smallest element=",sorted(tup)[1])

#28]Remove duplicates from a tuple
tup=(10,21,9,18,2,3,17,1)
s=set(tup)
print(s)
s=tuple(set(tup))
print(s)

#29]Find common elements between two tuples.
t1=(1,3,18,30,26,22,1,18)
t2=(11,22,33,44,18,30,1)
set1=set(t1)
set2=set(t2)
common=set1.intersection(set2)
print("Common Elements are:",common)