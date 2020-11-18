from collections import Counter

N=int(input())
S=[]

for _ in range(N):
    s=input()
    S.append(s)

c=Counter(S)
arr=c.most_common()

maxnum=arr[0][1]
ans=[]

for i in range(len(arr)):
    if arr[i][1]==maxnum:
        ans.append(arr[i][0])        
    else:
        break
FA=sorted(ans)
for j in FA:
    print(j)