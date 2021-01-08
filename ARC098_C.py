N=int(input())
S=input()

Wmax=0
Emax=0
W=[]
E=[]
for i in range (N):
    if S[i]=="W":
        Wmax+=1
        W.append(Wmax)
        E.append(0)
    else:
        Emax+=1
        E.append(Emax)
        W.append(0)

# print(Wmax,Emax)
# print("<- W:{}".format(W))
# print("-> E:{}".format(E))
ans=N
Wi=0
Ei=0
for i in range(N):
    tempWi=0
    tempEi=0
    if W[i]>0:
        Wi+=1
    else:
        Ei+=1
    WtoE=Wi
    if W[i]>0:
        WtoE-=1
    EtoW=Emax - Ei

    ans=min(ans,EtoW+WtoE)
    # print("i:{}/EtoW:{}/WtoE:{}".format(i,EtoW,WtoE))

print(ans)