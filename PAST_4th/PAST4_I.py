import bisect

N=int(input())
a=list(map(int,input().split()))

ac=[0]
for i in range (N):
    ac.append(ac[-1]+a[i])
full=ac[-1]
for j in range (N):
    ac.append(ac[-1]+a[j])
# print(ac)
t=ac[-1]//4
ans=full

for i in range (N+1):
    x=bisect.bisect(ac,ac[i]+t)
    # print(ac[i],ac[x])
    eat1=ac[x]-ac[i]
    rest1=full-eat1
    # '''
    # print(x,ac[x],ac[i])
    # print(eat1)
    # print(eat1,rest1)
# '''
    eat2=ac[x-1]-ac[i]
    rest2=full-eat2
    if x+1>=len(ac):
        eat3=0
    else:
        eat3=ac[x+1]-ac[i]
    rest3=full-eat3
    
    temp=min(abs(eat1-rest1),abs(eat2-rest2),abs(eat3-rest3))

    if ans>temp:
        ans=temp

    # print(temp)

print(ans)