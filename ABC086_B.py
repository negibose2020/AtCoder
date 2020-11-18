a,b=map(str,input().split())
num=int(a+b)

ans=num**0.5

if (ans//1)**2==num:
    print('Yes')
else:
    print('No')