from math import *

def QS(N):
    S=[]
    for i in range(len(sieve)):
        matrix=[]
        matrix.append([x for x in range(sieve[i])])
        matrix.append([x*x%sieve[i] for x in matrix[0]])
        matrix.append([(((x*x-N)%sieve[i])+sieve[i])%sieve[i] for x in matrix[0]])

        bits=""
        for j in range(len(matrix[2])):
            if matrix[2][j] in matrix[1]:
                bits+='1'
            else:
                bits+='0'
        S.append(bits)
        print(*matrix, sep="\n")
        print()
    print(S)

    low=floor(sqrt(N))+1
    high=ceil((N+1)/2)
    shift=[low%x for x in sieve]

    for i in range(len(S)):
        S[i]=S[i][shift[i]::]+S[i][:shift[i]:]
    print(f"S={S}, low={low}, high={high}, shift={shift}")
    
    
    necessaryNum=[]
    for i in range(low, high+1):
        isneed=""
        for j in range(len(S)):
            if S[j][(i-low)%len(S[j])] == "1":
                isneed+="1"
            else:
                isneed+="0"
        if isneed=="111":
           necessaryNum.append(i)
    print(f"necessaryNums=\n{necessaryNum}")
    
    for i in range(len(necessaryNum)):
        x=necessaryNum[i]
        if (x**2-N)==isqrt(x**2-N)**2:
            y=sqrt(x**2-N)
            print(x+y, x-y)

    
sieve=[4,5,7]
N=int(input())
QS(N)

#>_