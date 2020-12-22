N,K=map(int,input().split())

ls=[0]*(10**5+10)

for i in range (N):
    a,b=map(int,input().split())
    ls[a]+=b

ac_ls=[0]
for j in range(10**5+10):
    ac_ls.append(ac_ls[-1]+ls[j])
    if ac_ls[-1]>=K:
        print(j)
        exit()