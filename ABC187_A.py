# AtCoder Beginner Contest 187
# A - Large Digits

N,M=map(str,input().split())

n,m=0,0

for i in range (3):
    n+=int(N[i])
    m+=int(M[i])

print(max(n,m))