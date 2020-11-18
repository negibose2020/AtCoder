N,M=map(int,input().split())
a=input().split()
A=[]
for _ in a:
    A.append(int(_))
# print(N,M)
# print(A)

# N,M=4, 1
# A=[5, 4, 2, 1]

items=0
votes=sum(A)

for i in range(len(A)):
    if 4*M*A[i]>=votes:
        items+=1
    else:
        pass
if items>=M:
    print('Yes')
else:
    print('No')