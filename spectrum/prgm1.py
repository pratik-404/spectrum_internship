'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a=input("Enter the string : ")
b=""
for i in a:
    if i.islower():
        b+=i.upper()
    elif i.isupper:
        b+=i.lower()

print (b)