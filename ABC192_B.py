# SOMPO HD プログラミングコンテスト2021(AtCoder Beginner Contest 192)
# B - uNrEaDaBlE sTrInG

S=input()

for i in range(len(S)):
    L=S[i]
    if i%2==0:        
        if L.islower()==True:
            continue
        else:
            print("No")
            exit()
    else:
        if L.islower()==True:
            print("No")
            exit()
        else:
            continue

print("Yes")