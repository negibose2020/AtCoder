# AtCoder Regular Contest 108
# B - Abbreviate Fox

N=int(input())
s=input()

flg =True

while flg:
    flg=True
    S=s.replace("fox","")
    if S==s:
        flg=False
        print(len(S))
        exit()
    else:
        s=S

print(len(s))