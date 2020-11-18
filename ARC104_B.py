# AtCoder Regular Contest 104
# B - DNA Sequence

INPUTS=input().split()
N=int(INPUTS[0])
S=INPUTS[1]

ans=0

ansls=[]

for j in range (0,N):
    # print("j:{}{}".format(j,S[j]))
    for i in range(0,N+1-j):
        
        aA=S[j:j+i].count("A")
        aT=S[j:j+i].count("T")
        aC=S[j:j+i].count("C")
        aG=S[j:j+i].count("G")
        bA=S[j+i:(j+i)+i].count("A")
        bT=S[j+i:(j+i)+i].count("T")
        bC=S[j+i:(j+i)+i].count("C")
        bG=S[j+i:(j+i)+i].count("G")
        # print(j,i)
        # print(  S[j:j+i],
        #         S[j+i:(j+i)+i])
        # print(aA,aT,aC,aG,bA,bT,bC,bG)
        # print((aA==bT and aT==bA),)
        # print(len(S[j:j+i])==len(S[j+i:(j+i)+i]))
        # print((aA+aT+bA+bT)%2==0)
        # print("-------------")
        if len(S[j:j+i])==len(S[j+i:(j+i)+i]) and len(S[j:j+i])>0 :
            if (aA==bT and aT==bA) and (aC==bG and aG==bC):
                # print("hoge")
                # ansls.append([  S[j:j+i],
                # S[j+i:(j+i)+i]]
                # )
                ans+=1
                
# print(ansls)
print(ans)
