N,K=map(int,input().split())
_=input().split()
S=[]
for s in _:
    S.append((int(s)+1)/2) #初めから期待値で配列作成
# N,K=10,4
# S=[9.0, 7.0, 7.0, 6.5, 8.0, 10.5, 5.5, 7.0, 9.0, 6.0]

ans=sum(S[0:K])
temp=ans

for i in range(N-K):
    temp=temp-S[i]+S[i+K]
    if ans<temp:
        ans=temp
    else:
        pass
    
print(ans)