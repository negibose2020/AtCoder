# ABC158
# D - String Formation

def ChangeState(Is_normal):
    if Is_normal==True:
        return False
    else:
        return True


S=input()
Q=int(input())
Is_normal=True

h=''

for _ in range(Q):
    q = input()
    if len(q)== 1 :
        Is_normal = ChangeState(Is_normal)
    else:
        if q[2]=='1':
            if Is_normal==True:
                h=h+q[4]
            else :
                S=S+q[4]
        else :
            if Is_normal==True:
                S=S+q[4]
            else:
                h=h+q[4]
    # print(Is_normal, S)

h=h[::-1]
S=h+S

if Is_normal==False:
    S=S[::-1]

print(S)
