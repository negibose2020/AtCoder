# AtCoder Beginner Contest 183
# D - Water Heater

N,W=map(int,input().split())
yu=[0]*200004
for i in range (N):
    s,t,p=map(int,input().split())
    yu[s]+=p
    yu[t]-=p
# print(yu[:20])
ruiseki=[0]
for j in range (N+2):
    ruiseki.append(ruiseki[-1]+yu[j])
    # print(ruiseki)
    if ruiseki[-1]>W:
        print("No")
        exit()
print("Yes")


# imos法