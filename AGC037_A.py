# AtCoder Grand Contest 037
# A - Dividing a String

def f(S):
    ls=[]
    skip=False
    for i in range (len(S)):
        if skip==True:
            skip=False
            continue
        if i==0:
            skip=True
            ls.append(S[0:2])
        if i<len(S)-1:
            if S[i]==ls[-1]:
                skip=True
                ls.append(S[i:i+2])
            else:
                ls.append(S[i])
        if i==len(S)-1:
            if S[i]!=ls[-1]:
                ls.append(S[i])
            else:
                break
    print(ls)
    # return len(ls)


S=input()

ls=[]

ans=0
skip=False

for i in range (len(S)):
    print(skip)
    if i==0:
        ls.append(S[0])
    if skip==True:
        skip=False
        continue
        # pass
    if i<len(S)-1:
        if S[i]==ls[-1]:
            skip=True
            ls.append(S[i:i+2])
        else:
            ls.append(S[i])
    if i==len(S)-1:
        if S[i]!=ls[-1]:
            ls.append(S[i])
            ans=len(ls)
        else:
            ans=f(S)
print(ls)
print(ans)