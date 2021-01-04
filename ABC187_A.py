# AtCoder Beginner Contest 187
# A - Large Digits

N,M=map(str,input().split())

n=int(N[0])+int(N[1])+int(N[2])
m=int(M[0])+int(M[1])+int(M[2])

if n>=m:
    print(n)
else:
    print(m)