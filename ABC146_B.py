N=int(input())
S=input()

a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
anslist=[]

for i in range(len(S)):
    b=a.index(S[i])
    anslist.append(a[b+N])

ans="".join(anslist)
print(ans)