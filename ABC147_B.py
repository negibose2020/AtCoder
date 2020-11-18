S="abcdabc"

S=input()
h=len(S)//2
l=S[0:h]
r=S[h:]
Rr=r[::-1]

ans=0

for i in range(h):
    if l[i]==Rr[i]:
        pass
    else:
        ans+=1
print(ans)