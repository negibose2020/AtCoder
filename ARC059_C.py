N=int(input())
a=list(map(int,input().split()))

ans1=0
ans2=0
ans3=0
ans4=0

mn1=sum(a)//N
mn2=(sum(a)//N)+1
md1=sorted(a)[N//2]
if N>2:
    md2=sorted(a)[(N//2)]
for i in range (N):
    ans1+=(a[i]-mn1)*(a[i]-mn1)
    ans2+=(a[i]-mn2)*(a[i]-mn2)
    ans3+=(a[i]-md1)*(a[i]-md1)
    if N>2:
        ans4+=(a[i]-md2)*(a[i]-md2)
if N>2:
    print(min(ans1,ans2,ans3,ans4))
else:
    print((min(ans1,ans2,ans3)))