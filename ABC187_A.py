# AtCoder Beginner Contest 187
# A - Large Digits

N,M=map(str,input().split())

n=0
m=0

for i in range (3):
    n+=int(N[i])

for j in range (3):
    m+=int(M[j])

print(max(n,m))