# HHKB プログラミングコンテスト 2020
# B - Futon

H,W=map(int,input().split())
S=[]
s="#"*(W+2)
S.append(s)
for _ in range (H):
    s=input()
    s="#"+s+"#"
    S.append(s)
s="#"*(W+2)
S.append(s)

ans=0
for i in range (1,H+1):
    for j in range (1,W+1):
        if S[i][j]=="." and S[i][j+1]==".":
            ans+=1
        else:
            pass
        if S[i][j]=="." and S[i+1][j]==".":
            ans+=1
        else:
            pass

print(ans)
