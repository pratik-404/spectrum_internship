'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
c=0
a=[16,8,256,1024]
a.sort()
for i in range(-a[0],-1):
    k=(-1)*i
    for j in range(0,len(a)):
        if a[j]%k==0:
            c=c+1;
    if c==len(a):
        break;
print(k)        