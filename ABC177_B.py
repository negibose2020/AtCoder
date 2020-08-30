# AtCoder Beginner Contest 177
# B - Substring

S=input()
T=input()

Slen=len(S)
Tlen=len(T)

m=0

for i in range (Slen-Tlen+1):
    temp=0
    for j in range (Tlen):
        if T[j]==S[i+j]:
            temp+=1
        else:
            continue
    else:
        if temp>m:
            m=temp
print(Tlen-m)

        
