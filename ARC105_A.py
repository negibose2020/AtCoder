# AtCoder Regular Contest 105
# A - Fourtune Cookies


# A,B,C,D=map(int,input().split())
ls=list(map(int,input().split()))

N=4

for i in range(2**N):
    P=[]    
    for _ in range(N):
        if i>>_ & 1 ==1:
            P.append(1)
        else:
            P.append(0)
    E=0
    NE=0
    for j in range (4):
        if P[j]==1:
            E+=ls[j]
        else:
            NE+=ls[j]
    if E==NE:
        print("Yes")
        exit()
        

print("No")