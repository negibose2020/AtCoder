N=int(input())
S,T=map(str,input().split())

ans=[]
for i in range(N):
    ans.append(S[i])
    ans.append(T[i])

print(''.join(ans))