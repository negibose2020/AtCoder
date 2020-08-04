# AtCoder Grand Contest 019
# A - Ice Tea Store

Q,H,S,D=map(int,input().split())
N=int(input())

one=min (4*Q,2*H,S)
if N==1:
    print(one)
else :
    if 2*one<=D:
        print(N*one)
    else:
        if N%2==0:
            print((N//2)*D)
        else:
            print((N//2)*D+one)