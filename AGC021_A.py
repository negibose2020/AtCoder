N=int(input())
# N=100
n=str(N)
Length=len(n)

l=list(n)

if l[1:]==['9']*(Length-1):
    ans=int(n[0])+9*(Length-1)
else:
    ans=int(n[0])-1+9*(Length-1)

print(ans)