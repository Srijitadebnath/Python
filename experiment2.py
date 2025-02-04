'''1. Declare these variables (x, y and z) as integers. Assign a value of 9 to x,
Assign a value of 7 to y, perform addition, multiplication, division and subtraction on these two variables and Print out the result.'''
x=9
y=7
print(x+y)
print(x*y)
print(x/y)
print(x-y)
#2. Write a Program where the radius is taken as input to compute the area of a circle.
r=4
print(3.14*r*r)
'''3. Write a Python program to solve (x+y)*(x+y)
Test data : x = 4 , y = 3
Expected output: 49'''
x = 4
y = 3
print((x+y)*(x+y))

#4. Write a program to compute the length of the hypotenuse (c) of a right triangle using Pythagoras theorem.
height=5
base=3
hy=height**2+base**2
print(hy)
#5. Write a program to find simple interest.
p=50000
r=15
t=4
si=(p+r+t)/100
print(si)
#6. Write a program to find area of triangle when length of sides are given.
l=7
b=8
area=1/2*l*b
print(area)
#7. Write a program to convert given seconds into hours, minutes and remaining seconds.
sec = int(input("Enter the number of seconds: "))

hours = sec//3600
minutes = (sec% 3600)//60
rem_sec = sec % 60
print(f"{hours} {minutes} {rem_sec}")

#8. Write a program to swap two numbers without taking additional variable.
a=5
b=8
a,b=b,a
print(a,b)
#9. Write a program to find sum of first n natural numbers.
n=int(input("Enter the numbers:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("sum of n terms of natural number",sum)
#10. Write a program to print truth table for bitwise operators( & , | and ^ operators)
print("Truth Table for bitwise operator")
print("A\tB\tA&B\tA|B\tA^B")
for a in range(2):
    for b in range(2):
          print(f"{a}\t{b}\t{a&b}\t{a|b}\t{a^b}")
#11. Using membership operator find whether a given number is in sequence (10,20,56,78,89)
seq=(10,20,56,78,89)
num=int(input("enter the number"))
if num in seq:
    print(f"{num} sin sequence")
else:
    print(f"{num} not in sequence")
#12. Using membership operator find whether a given character is in a string.

s="Srijita"
n=input("enter the string:")
for i in s:
    if n in s:
        print(f"{n} is in the string")
    else:
        print(f"{n} is not in string")
