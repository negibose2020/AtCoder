N=int(input())
S=input()

ans=0

for i in range (1000):
    tempS=S
    pin=str(i).zfill(3)
    t1=pin[0]
    t2=pin[1]
    t3=pin[2]
    if tempS.count(t1)>=1:
        tempS=tempS[tempS.find(t1)+1:]
    else:
        continue

    if tempS.count(t2)>=1:
        tempS=tempS[tempS.find(t2)+1:]
    else:
        continue

    if tempS.count(t3)>=1:
        ans+=1
    else:
        continue

print(ans)