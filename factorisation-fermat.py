from math import *

def factor(N):
    x=ceil(sqrt(N))
    y2=x*x-N
    while not y2==isqrt(y2)**2:
        x+=1
        y2=x*x-N
    y=sqrt(y2)
    return x-y, x+y

print(factor(int(input())))

#>_