N,Q=map(int,input().split())
S=input()

ac_ls=[0]
# ac_ls=[[0,0,0]]

for i in range (1,N):
    if S[i-1]=="A" and S[i]=="C":
        ac_ls.append(ac_ls[-1]+1)
        # ac_ls.append([S[i-1],S[i],ac_ls[-1][2]+1])
    else:
        ac_ls.append(ac_ls[-1])
        # ac_ls.append([S[i-1],S[i],ac_ls[-1][2]])
else:
    ac_ls.append(ac_ls[-1])

    # print(ac_ls)

for _ in range (Q):
    l,r=map(int,input().split())
    if ac_ls[l]==ac_ls[l-1]+1:
        mi=ac_ls[l]
    else:
        mi=ac_ls[l]+1
    if ac_ls[r]==ac_ls[r-1]+1:
        ma=ac_ls[r]-1
    else:
        ma=ac_ls[r]
    print(ma-mi+1)

# print(ac_ls)