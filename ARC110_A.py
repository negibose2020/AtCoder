# 鹿島建設プログラミングコンテスト2020（AtCoder Regular Contest 110）
# A - Redundant Redundancy

import bisect

N=int(input())
if N>=29:
    print(9316358251201)
    exit()

ans=1

pnums=[2,3,4,5,7,9,11,13,16,17,19,23,25,29,31]

a=bisect.bisect(pnums,N)
pls=pnums[:a]

# print(pls)
for i in range (len(pls)):
    ans*=pls[i]

ans=ans+1
print(ans)

'''
for i in range (2,N+1):
    print(ans%i)
'''
'''

def f(N):

    import bisect

    # N=int(input())

    ans=1

    pnums=[2,3,4,5,7,9,11,13,16,17,19,23,25,29]

    a=bisect.bisect(pnums,N)
    pls=pnums[:a]

    # print(pls)
    for i in range (len(pls)):
        ans*=pls[i]

    ans=ans+1
    print(N,ans)

    for i in range (2,N+1):
        if ans%i==1:
            pass
        else:
            print(N,ans%i)
    else:
        print(N,ans,10**13+1>ans)

for i in range (31):
    f(i)

b=93163582512001
print(10**13+1>9316358251201)

for i in range (2,30):
    print(9316358251201%i)
    '''