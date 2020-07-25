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

for _ in range(Q):
    q = input()
    if len(q)== 1 :
        Is_normal = ChangeState(Is_normal)
    else:
        if q[2]=='1':
            if Is_normal==True:
                S=q[4]+S
            else :
                S=S+q[4]
        else :
            if Is_normal==True:
                S=S+q[4]
            else:
                S=q[4]+S
    # print(Is_normal, S)
if Is_normal==False:
    S=S[::-1]
print(S)
