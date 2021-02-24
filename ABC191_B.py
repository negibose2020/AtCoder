# AtCoder Beginner Contest 191
# B - Remove It

n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=[]
for i in range (n):
    if a[i]==x:
        pass
    else:
        ans.append(str(a[i]))
print(" ".join(ans))