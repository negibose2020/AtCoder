N,K=map(int,input().split())    
p=list(map(int,input().split()))

l=sorted(p)[:K]
print(sum(l))