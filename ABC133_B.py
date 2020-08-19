# AtCoder Beginner Contest 133
# B - Good Distance

def f(a,b,d):
    X=0
    for i in range (d):
        X+=(a[i]-b[i])**2
    return X**0.5


from itertools import combinations

ans =0

N,D=map(int,input().split())
ls=[]
for _ in range(N):
    p=list(map(int,input().split()))
    ls.append(p)

c=list(combinations(ls,2))
# print(c)

for i in range (len(c)):
    a=f(c[i][0],c[i][1],D)
    if a==a//1:
        ans+=1
    

print(ans)
