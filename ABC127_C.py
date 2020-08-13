# AtCoder Beginner Contest 127
# C - Prison

N,M= map(int,input().split())

Gates=[]
for i in range (M):
    l,r=map(int,input().split())
    Gates.append([l,r])

ans =0

for i in range (1,N+1):
    for j in range (M):
        # print(i,Gates[j])
        # print(Gates[j][0]<=i and i<=Gates[j][1]) 
        if Gates[j][0]<=i and i<=Gates[j][1]:
            pass
        else:
            break
    else:
        ans+=1
    # print(ans)

print(ans)
