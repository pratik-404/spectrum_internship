'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
c=0
L =[]
n=int(input("Enter the number: "))
for i in range(2,n+1):
    for j in range(2,int(i**0.5)+1):
        if int(i%j)==0:
            c=c+1
            break
    if c==0:
        L.append( i )
    c=0
print(*L ,sep=",")