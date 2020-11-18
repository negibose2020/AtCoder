N,M=map(int,input().split())
ans=[-1]*(N+1)
for i in range(M):
    s,c=map(int,input().split())
    if ans[s]==-1 :
        ans[s]=c
    elif ans[s]==c :
        pass
    else:
        print('-1')
        exit()

if N>=2 and ans[1]==0:
    print('-1')
    exit()
elif N>=2 and ans[1]==-1: #ここが間違ってた。
    ans[1]=1
else:
    pass

for j in range(len(ans)):
    if ans[j] == -1:
        ans[j] = 0

if N==1:
    FA=ans[-1]
elif N==2:
    FA=10*ans[-2]+ans[-1]
else:
    FA=100*ans[-3]+10*ans[-2]+ans[-1]
print(FA)