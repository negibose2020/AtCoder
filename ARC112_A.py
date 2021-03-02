# AtCoder Regular Contest 112
# A - B = C

T=int(input())

for _ in range (T):

    L,R=map(int,input().split())

    temp=R-L-L+1
    if temp<0:
        print(0)
        continue
    ans=(temp*(temp+1))//2

    print(ans)
