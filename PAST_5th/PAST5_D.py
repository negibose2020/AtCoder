# 第五回 アルゴリズム実技検定
# D - リーディングゼロ

import bisect

N=int(input())
ls_origin=[]
st=set()

for i in range (N):
    s=input()
    s_num=int(s)
    ls_origin.append(s)
    
    st.add(s_num)

targetnumlist=list(st)
targetnumlist.sort()

ls2d=[[]for _ in range (len(st))]

for e in ls_origin:
    s_num=int(e)
    s_len=len(e)
    x=bisect.bisect(targetnumlist,s_num)
    ls2d[x-1].append([e,s_len])

# print(ls2d)

for i in range (len(targetnumlist)):
    nums4printing=ls2d[i]
    printingnums=sorted(nums4printing, key=lambda x:x[1], reverse=True)
    for prnt in printingnums:
        print(prnt[0])
