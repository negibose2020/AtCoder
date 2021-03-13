# パナソニックプログラミングコンテスト（AtCoder Beginner Contest 195）
# B - Many Oranges

A,B,W=map(int,input().split())

W*=1000

ans=[]

# if A>W:
#     print("UNSATISFIABLE")
#     exit()
# if W%A>A:
#     print("UNSATISFIABLE")
#     exit()

for i in range (1000000):
    WA=A*i
    if WA>W:
        break
    RW=W-WA
    if RW==0:
        ans.append(i)
        # print(0)
    # elif RW<=B:
    #     ans.append(i+1)
    #     print(111,i+1,i)
    else:
        if RW%B==0:
            ans.append(i+RW//B)
            # print(222,i+RW//B,i)
        elif RW%B >= A:
            ans.append(i+RW//B +1)
            # print(333,i+RW//B +1,i)
        else:
            pass


for j in range (1000000000000):
    WB=B*j
    if WB>W:
        break
    RW=W-WB
    if RW==0:
        ans.append(j)
        # print(444,j)
    # elif RW>=A:
    #     ans.append(j+1)
    #     print(j+1)
    else:
        if RW%A==0:
            ans.append(j+RW//A)
            # print(555,j+RW//A)
        else:
            if RW%A<A:
                pass
                # ans.append(j+RW//A)
                # print(666,j+RW//A)
            else:
                pass


if len(ans)==0:
    print("UNSATISFIABLE")
    exit()
    
# print(ans)
ans.sort()
print(ans[0], ans[-1])