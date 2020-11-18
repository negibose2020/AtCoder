# N=int(input())
N= 100

Ans=0
for i in range(1,N+1):
    if i%3==0 or i%5==0:
        pass
    else:
        Ans+=i
print(Ans)