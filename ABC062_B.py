# AtCoder Beginner Contest 062
# B - Picture Frame

H,W=map(int,input().split())
ans=["#"*(W+2)]
for i in range (H):
    p=input()
    _="#"+p+"#"
    ans.append(_)
ans.append("#"*(W+2))

for i in range (H+2):
    print(ans[i])