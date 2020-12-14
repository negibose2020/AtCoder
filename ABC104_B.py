# AtCoder Beginner Contest 104
# B - AcCepted

S=input()

if S[0]!="A":
    print("WA")
    exit()
s=S[2:-1]
cntC=0
for i in range (len(s)):
    if s[i]=="C":
        cntC+=1
if cntC!=1:
    print("WA")
    exit()
for j in range (1,len(S)):
    if S[j]=="C":
        pass
    else:
        if str.lower(S[j])!=S[j]:
            print("WA")
            exit()

print("AC")