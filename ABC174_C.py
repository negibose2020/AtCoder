# AtCoder Beginner Contest 174
# C - Repsept

K=int(input())

modsevens=[7]

if K==7 or K==1:
    print(1)
    exit()
else:
    pass

for i in range (1,K):
    a=(modsevens[-1] *10+7)%K
    
    if a==0:
        print(i+1)
        exit()
    else:
        modsevens.append(a)

print(-1)