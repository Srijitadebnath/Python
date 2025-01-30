#palindrome number of a string
s=input("enter the string :")
sl=list(s)
t1=tuple(sl)
print(t1)
rev=t1[::-1]
if t1==rev:
    print("s is a palindrome no")
else:
    print("s is not a palindrome no")

#palindrome of a  given list
l=[1,"abc","abc",1]
print(l)
rev=l[::-1]
if l==rev:
    print("s is a palindrome no")
else:
    print("s is not a palindrome no")

#palindrome using in-build function
l=[1,"abc","abc",1]
print(l)
print(l.reverse())


     


