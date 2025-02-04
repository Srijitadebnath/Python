#1. Check whether given number is divisible by 3 and 5 both.
n=int(input("enter the number:"))
if(n%3==0 and n%5==0):
    print(f"{n} is divisible by both 3 and 5")
else:
    print(f"{n} is not divisible by either 3 or 5")
#2. Check whether a given number is multiple of five or not.
n=int(input("enter the number:"))
if(n%5==0):
    print(f"{n} is multiple of 5")
else:
    print(f"{n} is not multiple of 5")
#3. Find the greatest among two numbers. If numbers are equal than print “numbers are equal”.
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
if(a>b):
    print(f"{a} is greater than {b}")
else:
    print(f"both {a} and {b} are equal")
#4. Find the greatest among three numbers assuming no two values are same.
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if(a>b and a>c):
    print(f"{a} is greater the {b} and {c}")
elif (b>a and b>c):
    print(f"{b} is greater the {a} and {c}")
else:
    print(f"{c} is greater the {a} and {b}")

#5. Check whether the quadratic equation has real roots or imaginary roots. Display the roots.
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

determinant = b**2 - 4*a*c
if determinant > 0:
    root1 = (-b + (determinant**0.5)) / (2*a)
    root2 = (-b - (determinant**0.5)) / (2*a)
    
    print("The quadratic equation has real and distinct roots.")
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")
elif determinant == 0:
    root = -b / (2*a)
    
    print("The quadratic equation has real and equal roots.")
    print(f"Root: {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = (-determinant**0.5) / (2*a)
    
    print("The quadratic equation has imaginary roots.")
    print(f"Root 1: {real_part} + {imaginary_part}i")
    print(f"Root 2: {real_part} - {imaginary_part}i")

#6. Find whether a given year is a leap year or not.
year=int(input("enter the years:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
else:
    primt(f"{year} is not a leap year")


'''7. Write a program which takes any date as input and display next date of the calendar
e.g.
I/P: day=20 month=9 year=2005
O/P: day=21 month=9 year 2005'''

d=int(input("enter day:"))
m=int(input("enter the month:"))
y=int(input("enter the year:"))

if m in [1,3,5,7,8,10,12]:
    days_in_month=31

#for lear year
elif m==2:
    if y%4==0 and(y%100!=0 or y%400==0):
        days_in_month=29
    else:
       days_in_month=28
#monthhaving dates 30
else:
    days_in_month=30
if d < days_in_month:
    next_day=d+1
    next_month=m
    next_year=y
else:
    if m<12:
        next_day=1
        next_month=m+1
        next_year=1
    else:
        next_dat=1
        next_month=1
        next_year=y+1
print(f"Next date:{next_day}-{next_month}-{next_year}")
'''8. Print the grade sheet of a student for the given range of cgpa. Scan marks of five subjects and calculate the percentage.
CGPA=percentage/10
CGPA range:
0 to 3.4 -> F
3.5 to 5.0->C+
5.1 to 6->B
6.1 to 7-> B+
7.1 to 8-> A
8.1 to 9->A+
9.1 to 10-> O (Outstanding)
Sample Gradesheet
Name: Rohit Sharma
Roll Number: R17234512 SAPID: 50005673
Sem: 1 Course: B.Tech. CSE AI&ML
Subject name: Marks
PDS: 70
Python: 80
Chemistry: 90
English: 60
Physics: 50
Percentage: 70%
CGPA:7.0
Grade:'''

name = "Srijita"
roll_number = "2410110381"
sap_id = "590013103"
sem = "1"
course = "B.Tech. CSE "

marks = [70,90, 60, 50]
subjects = ["Programming c", "Mathematics" "Managing self", "Physics"]

print("Name:", name)
print("Roll Number:", roll_number)
print("SAP ID:", sap_id)
print("Sem:", sem)
print("Course:", course)
print("Subject Name\tMarks")

for i in range(len(subjects)):
    print(subjects[i], "\t", marks[i])

percentage = sum(marks) / len(marks)
cgpa = percentage / 10

if cgpa >= 9.1:
    grade = "O (Outstanding)"
elif cgpa >= 8.1:
    grade = "A+"
elif cgpa >= 7.1:
    grade = "A"
elif cgpa >= 6.1:
    grade = "B+"
elif cgpa >= 5.1:
    grade = "B"
elif cgpa >= 3.5:
    grade = "C+"
else:
    grade = "F"

print("Percentage:", percentage, "%")
print("CGPA:", cgpa)
print("Grade:", grade)

