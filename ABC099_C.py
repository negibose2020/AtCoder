# AtCoder Regular Contest 099
# C - Minimization 

N,K =map(int,input().split())
A=list(map(int,input().split()))

ans=0

a=N-K
ans+=1

if a>0:
    ans+=a//(K-1)
    if a%(K-1)==0:
        pass
    else:
        ans+=1
else:
    pass

print(ans)

# N,K =map(int,input().split())
# A=list(map(int,input().split()))

# ans=0

# a=N-K
# ans+=1

# while a>0:
#     a+=1
#     ans+=1
#     a=a-K
# print(ans)
