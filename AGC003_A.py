# AtCoder Grand Contest 003
# A - Wanna go back home

s=input()

N=0
W=0
S=0
E=0

for _ in s:
    if _=="N":
        N+=1
    if _=="W":
        W+=1
    if _=="S":
        S+=1
    if _=="E":
        E+=1

if N==0 and S==0 and W==0 and E==0:
    print("Yes")
    exit()
if N*S>0 and W*E>0:
    print("Yes")
    exit()
if N*S>0 and W==0 and E==0:
    print("Yes")
    exit()
if W*E>0 and N==0 and S==0:
    print("Yes")
    exit()
print("No")