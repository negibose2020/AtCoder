S=input()
# S="akasakaakasakasakaakas"

for i in range(1,len(S)):
    s=S[:-1*i]
    if len(s)%2==0:
        head=s[:len(s)//2]
        tail=s[len(s)//2:]
        if head==tail:
            print(len(s))
            break
        else:
            pass
    else:
        continue
