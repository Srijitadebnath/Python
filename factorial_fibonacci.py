##factorial using function
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
n=int(input("enter the number:"))
print(factorial(n))

#fibonacci series using function
def fibonacci(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,b+a
    return a,b
n=int(input("enter the number:"))
fibonacci(n)



    
#factrial using recursion

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter the number:"))
print(factorial(n))


#fibonacci using recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("enter the number:"))
for i in range(n):
   print(fibonacci(i))
