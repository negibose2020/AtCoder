# AtCoder Beginner Contest 127
# C - Prison
N,M= map(int,input().split())

ls=[0]*(10**5+100)

for i in range (M):
    r,l = map(int,input().split())
    ls[r+1]+=1
    ls[l+2]-=1
    
ls2=[0]
for i in range(10**5+100):
    a=ls2[-1]+ls[i]
    ls2.append(a)

# print(ls2)
ans=0
for j in range(10**5+101):
    if ls2[j]==M:
        ans+=1
    
print(ans)