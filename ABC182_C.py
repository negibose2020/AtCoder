# AtCoder Beginner Contest 182
# C - To 3

n=input()
originr=int(n)%3
if originr==0:
    print(0)
    exit()

N=list(map(int,n))
r1=0
r2=0

for e in N:
    r=e%3
    if r==1:
        r1+=1
    elif r==2:
        r2+=1

if originr==1:
    if r1>0:
        ans=1
    else:
        ans=2
else:
    if r2>0:
        ans=1
    else:
        ans=2
if ans==len(N):
    print(-1)
else:
    print(ans)

'''
    print(0)
    exit()

ans=abs(M1-M2)%3

# if M1>M2:
#     ans=(M1-M2)%3
# else:
#     ans=(M2-M1)%3

if ans==len(N):
    print(-1)
else:
    print(ans)
'''
'''



N=input()
r1=0
r2=0
Rls1=[]
Rls2=[]

if int(N)%3==0:
    print(0)
    exit()
for e in N:
    if int(e)%3==0:
        pass
    elif int(e)%3==1:
        r1+=1
        Rls1.append(int(e))
    else:
        r2+=1
        Rls2.append(int(e))
print(Rls1)
print(Rls2)
print(r1,r2)

if r2<r1:
    r1%=3
    r2%=3
    # print(r1,r2)
    ans=abs(r1-r2)
    if ans==len(N):
        print(-1)
    else:
        print(ans)
else:
    ans=(r2-r1)%3
    if ans==len(N):
        print(-1)
    else:
        print(ans)
   ''' 
'''
if r1==r2:
    print(0)
    exit()

ans=abs(r1-r2)%3
if ans==len(N):
    print(-1)
else:
    print(ans)
'''