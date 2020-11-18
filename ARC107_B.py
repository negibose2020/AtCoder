# AtCoder Regular Contest 107
# 

N,K=map(int,input().split())

ans=0


if K>=0:
    '''
    # for i in range (K+2,2*N+1):
    #     ab=i
    #     # ab-1 通り
    #     cd=ab-K
    #     ans+=((ab-(N-1))*(cd-(N-1)))//2
    #     # ans+=ab-N
    #     # ans+=cd-N
    #     print(ab,cd)
'''

    for i in range (K+2,2*N+1):
        ab=i
        # ab-1 通り
        cd=ab-K
        ans+=((ab-(N-1))*(cd-(N-1)))//2
        # ans+=ab-N
        # ans+=cd-N
        print(ab,cd)

else :  
    ansls=[]
    for i in range (2,2*N+1-K):
        ab=i
        cd=ab-K
        ans+=(ab-2)*(cd-2)
        # ans+=cd-2
        ansls.append([ab,cd])

# print(ansls)
print(ans)
