'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
a=[12,4,5,19,11]
sum=0
n=int(input("Enter the number: "))
for i in range(0,len(a)):
    for j in range(i,len(a)):
        for k in range(j,len(a)):
            sum=0
            if i!=j and i!=k and j!=k:
                sum=a[i]+a[j]+a[k]
            if sum==n:
                print(a[i],a[j],a[k])
            