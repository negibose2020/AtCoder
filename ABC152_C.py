N=int(input())
P=input().split()
Pn=[]
Pn.append(int(P[0]))

count=1
nowmin=Pn[0]

for i in range(1,len(P)):
    if int(P[i])<nowmin:
        count+=1
        nowmin = int(P[i])
    
print(count)
