#WAP to display last digit of given number
num=int(input("Enter a number:"))
last_digit=num%10
print(f"last digit ={last_digit}")

#WAP to remove last digit of given number
num=int(input("Enter a number:"))
remove=num//10
print(f"Remove last digit={remove}")

#WAP to find the sum of first N numbers
n=int(input("Enter a number:"))
sum=n*(n+1)//2
print(f"Sum of n number={sum}")

#WAP to swap 2 numbers
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
a,b=b,a
print("After Swaping")
print("a=",a)
print("b=",b)

#WAP to swap 2 numbers without 3 rd variable
a=int(input("Enter first number="))
b=int(input("Enter Second number="))
a=a+b
b=a-b
a=a-b
print("After Swapping:")
print("a=",a)
print("b=",b)

#WAP to calculate the total amount for the given quantity of fruits purchased
price=int(input("Enter Price of fruit per kg:"))
Quantity=int(input("Enter quantity purchased:"))
total=price*Quantity
print("total amount=",total)

#WAp to find the total salary for the given basic salary
basic_salary=int(input("Enter basic salary:"))
hra=basic_salary*0.20
da=basic_salary*0.10
total_salary=basic_salary+hra+da
print("Total salary=",total_salary)

#WAP to calculate Area of Circle (3.14*r*r)
radius=int(input("Enter radius:"))
area=3.14*radius*radius
print("Area of circle=",area)

#WAP to calculate area of Triangle (A=1/2*b*h)
base=float(input("Enter Base:"))
height=float(input("Enter Height:"))
area=0.5*base*height
print("Area of Triangle=",area)


