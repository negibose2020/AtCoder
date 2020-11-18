N=int(input())
An=list(map(int,input().split()))

B=0

for A in An:
    B+=1/A

print(1/B)
