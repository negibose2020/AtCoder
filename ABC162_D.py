from collections import Counter

N=int(input())
S=input()

C=Counter(S)
r=C['R']
g=C['G']
b=C['B']

ans=r*g*b
# print(r,g,b)

for i in range(N-2):
    for j in range(i+1,N-1):
        if S[i]==S[j]:
            continue
        
        k=2*j-i
        if k>=N:
            continue
        if S[j]!=S[k] and S[k]!=S[i] : #S[i],S[j],S[k]が全て異なる状態から、j-i=k-jの場合を引く。
            ans-=1

print(ans)