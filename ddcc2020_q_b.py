# DISCO presents ディスカバリーチャンネル コードコンテスト2020 予選
# B - Iron Bar Cutting

N=int(input())
A=list(map(int,input().split()))

aA_n=[0]
for i in range (N):
    aA_n.append(A[i]+aA_n[-1])
aA_n=aA_n[1:]


rA=A[::-1]
aA_r=[0]
for i in range (N):
        aA_r.append(rA[i]+aA_r[-1])
aA_r=aA_r[1:]
aA_r=aA_r[::-1]

ans=aA_n[-1]
for i in range (N-1):
    _tempans=abs(aA_n[i]-aA_r[i+1])
    if _tempans<ans:
        ans=_tempans

print(ans)