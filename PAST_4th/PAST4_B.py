# B - 電卓
import decimal

X,Y=map(int,input().split())

if Y==0:
    print("ERROR")
    exit()
if X%Y==0:
    print("{}.00".format(X//Y))
    exit()

ans=X/Y
ansls=list(str(ans))
pindex=ansls.index(".")
if len(ansls)-1-pindex==1:
    print("".join(ansls)+"0")
    exit()
print("".join(ansls[:pindex+3]))