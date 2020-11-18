N=int(input())
a=list(map(int,input().split()))

l=[0]*((10**5)+2)

for v in a:
    l[v]+=1
    l[v+1]+=1
    l[v+2]+=1

print(max(l))


'''
参考URL
https://arcslab.hatenablog.jp/entry/ABC072
>数xに対して、count[x-1]++; count[x]++; count[x+1]++;をしていった後、どのcount[]が最大の値かを調べればOK。
>イメージとしては「長さnの直線上に積み木を3つずつ積んでいく」感じ。一番高く積み上がった場所が答え。
'''
'''
参考URL2
http://prdc.hatenablog.com/entry/2017/09/04/223025
>Pythonでの上記イメージの記述
'''