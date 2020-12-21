N,K=map(int,input().split())
R,S,P=map(int,input().split())
T=input()

ans=0

myhands=[]
for i in range (N):
    if i<K:
        if T[i]=="r":
            ans+=P
            myhands.append("P")
        elif T[i]=="s":
            ans+=R
            myhands.append("R")
        else:
            ans+=S
            myhands.append("S")
    else:
        if T[i]=="r":
            if myhands[i-K]!="P":
                ans+=P
                myhands.append("P")
            else:
                ans+=0
                myhands.append("A")
        elif T[i]=="s":
            if myhands[i-K]!="R":
                ans+=R
                myhands.append("R")
            else:
                ans+=0
                myhands.append("A")
        else:
            if myhands[i-K]!="S":
                ans+=S
                myhands.append("S")
            else:
                ans+=0
                myhands.append("A")
# print(myhands)
print(ans)