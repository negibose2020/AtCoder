N=int(input())
a=list(map(int,input().split()))
A=[0]
A.extend(a)
A.append(0)

cost=[]
for i in range (N+1):
    cost.append(abs(A[i]-A[i+1]))
# print(A)
# print(cost)
totalcost=sum(cost)

for i in range (1,N+1):
    print(totalcost-cost[i]-cost[i-1]+abs(A[i-1]-A[i+1]))
