import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
# base = comb(5,3)
# print(base) # 10

N,P=map(int,input().split())
A=list(map(int,input().split()))

e=[]
o=[]
for a in A:
    if a%2==0:
        e.append(a)
    else:
        o.append(a)
# print(e,o)
# print(193/32)
ans=0

if P==1:
    if len(o)==0:
        print(0)
        exit()
    else:
        for i in range (len(e)+1):
            for j in range (1,len(o)+1,2):
                ans+=comb(len(e),i)*comb(len(o),j)

if P==0:
    for i in range (len(e)+1):
        for j in range (0,len(o)+1,2):
            ans+=comb(len(e),i)*comb(len(o),j)

print(ans)
exit()