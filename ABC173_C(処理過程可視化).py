import numpy as np

H,W,K=map(int,input().split())
b=[]
for i in range(H):
    _=input()
    temp=_.replace('#','1').replace('.','0')
    b.append(list(map(int,temp)))

area=np.array(b)
# print(Arr)

ans=0
print('Start  >'+'>>'*42)

for h in range (2**H):
    select_H=[] #削除する行の組合わせを取得
    print("")
    print("# "*5 + 'pattern{0}'.format(h+1) + " # "*25)    
    print('↓  基の状態')
    print(area)

    for i in range (H):
        if (h>>i) & 1==1:
            select_H.append(1)
        else:
            select_H.append(0)
    sHarr=np.array(select_H)
    delsHarr=np.where(sHarr==1) #削除する行のindexを取得
    area_afterDelsH=np.delete(area,delsHarr,axis=0) #エリアから行を削除する。
            # 以下、行が削除された各パターンについて、列を削除していく。
    
    print('             {0}  ← 今回削除する 行index'.format(delsHarr))

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
        print('- '*10 + 'pattern{0}-{1}'.format(h+1,w+1)+ ' - '*21)

        print('↓  行削除後')
        print('{0}'.format(area_afterDelsH))
        # print('                 '+". "*2 + 'pattern{0}-{1}'.format(h+1,w+1) + ". "*10)
        # print('                 ↓_今回削除する 列index')
        print('                  {0}  ← 今回削除する 列index'.format(delsWarr))

        # print('削除行：{0}、削除列{1}'.format(delsHarr,delsWarr))
        print('↓  列も削除後')
        print('{0}'.format(area_afterDelsHsW))
        print('1"がある個数は、{0}個。 よって、ans + = {1}'.format(np.sum(area_afterDelsHsW),np.sum(area_afterDelsHsW)==K))
        print("")
        if np.sum(area_afterDelsHsW)==K:
            ans+=1

print('')
print('...')
print("最終的な答えは、{0}".format(ans))
print('<<'*43 + '  enD')
# print(ans)