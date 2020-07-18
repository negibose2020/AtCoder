import numpy as np

H,W,K=map(int,input().split())
b=[]
for i in range(H):
    _=input()
    temp=_.replace('#','1').replace('.','0')
    b.append(list(map(int,temp)))

area=np.array(b)

ans=0

for h in range (2**H):
    select_H=[] #削除する行の組合わせを取得

    for i in range (H):
        if (h>>i) & 1==1:
            select_H.append(1)
        else:
            select_H.append(0)
    sHarr=np.array(select_H)
    delsHarr=np.where(sHarr==1) #削除する行のindexを取得
    area_afterDelsH=np.delete(area,delsHarr,axis=0) #エリアから行を削除する。
            # 以下、行が削除された各パターンについて、列を削除していく。

    for w in range (2**W):
        select_W=[] #削除する列の組合わせを取得
        for j in range (W):
            if (w>>j) &1 ==1:
                select_W.append(1)
            else:
                select_W.append(0)
        sWarr=np.array(select_W)
        delsWarr=np.where(sWarr==1) #削除する列のindexを取得
        area_afterDelsHsW=np.delete(area_afterDelsH,delsWarr,axis=1)

        if np.sum(area_afterDelsHsW)==K:
            ans+=1

print(ans)