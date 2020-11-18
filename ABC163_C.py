N=int(input())
a=input().split()
A=[]
for _ in a:
    A.append(int(_))
E=[0]*(N+1)

for i in range (len(A)):
    _boss=A[i]
    E[_boss]+=1

for j in range(1,len(E)):
    print(E[j])
