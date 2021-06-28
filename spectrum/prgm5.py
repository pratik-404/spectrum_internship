'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a=0
s=0
k=1
n=int(input("Enter the number: "))
while(1):
    s=0
    for i in range(1,int(k/2)+1):
        if k%i == 0 and k!=i:
            s=s+i
    if s==k:
        print(k,end=',')
        a=a+1
        if a==n:
            break
    k=k+1