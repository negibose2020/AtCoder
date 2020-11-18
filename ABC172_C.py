import bisect

N,M,K=map(int,input().split())
list_a=list(map(int,input().split()))
list_b=list(map(int,input().split()))

#Aの山の累積和を作成(Kを超えたらSTOP)
totaltime_a=[0]
for a in list_a:
    temp_a=totaltime_a[-1]+a
    if temp_a>K:
        break
    else:
        totaltime_a.append(temp_a)

totaltime_b=[0]
for b in list_b:
    totaltime_b.append(totaltime_b[-1]+b)

ans=0

for i in range (len(totaltime_a)):
    Kb=K-totaltime_a[i]
    j=bisect.bisect_right(totaltime_b,Kb)-1
    if i+j>ans:
        ans=i+j
    else:
        pass

print(ans)