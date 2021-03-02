# AtCoder Regular Contest 113
# A - A*B*C

K=int(input())
# K=2*10**5
ans=0

for a in range (1,K+1):
    for b in range (1,K+1):
        x=a*b
        if x>K:
            break
        ans+=K//x
print(ans)