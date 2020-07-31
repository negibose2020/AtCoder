# AtCoder Beginner Contest 135
# B - 0 or 1 Swap

N=int(input())
p=list(map(int,input().split()))

S={}
s=N+1

for i in range (N):
    if p[i]==i+1:
        pass
    else :
        S[i+1]=p[i]
        s=i+1


if len (S)==0:
    print('YES')
    exit()
elif len(S)>2:
    print('NO')

else:
    n=S[s]
    if S[n]==s:
        print('YES')
    else:
        print('NO')