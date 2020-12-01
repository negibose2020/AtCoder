N=int(input())
S=list(input())

l=S.index("#")
r=S[::-1].index("#")
# print(S)
# if l+r==N-1:
#     print(l,r)
#     exit()
# print(l)
# print(r)


S2=S[::-1]  #参照用
S3=S[::-1]  #更新用
for i in range (N):
    if S2[i]=="#":
        for j in range (l+1):
            if i+j<=N:
                S3[i+j]="#"
                # print(S3,i,j)
            else:
                break

S4=S3[::-1] #参照用
S5=S3[::-1] #更新用
for i in range (N):
    if S4[i]=="#":
        for j in range (r+1):
            if i+j<=N:
                S5[i+j]="#"
            else:
                break

# print(S5)
S6=S5[::-1]
p1=0
temp1=0
for i in range (N):
    if S6[i]==".":
        temp1+=1
    else:
        if temp1>p1:
            p1=temp1
        temp1=0
'''
S=S[::-1]
p2=0
temp2=0
for i in range (N):
    if S[i]==".":
        temp2+=1
    else:
        if temp2>p2:
            p2=temp2

print(l,r+min(p1,p2))
'''
print(l+p1,r)