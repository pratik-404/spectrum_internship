'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def print_stars(x): 
    i=0
    y=x
    while(x>0):
        
        print (" "*i,"* "*x,sep="")
        x-=1
        i+=1
    j=2
    x=y
    while(j<=x):
        print (" "*(y-2),"* "*j,sep="")
        y=y-1
        j+=1

print_stars(5)