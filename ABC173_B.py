N=int(input())
dic={}
dic['AC']=0
dic['WA']=0
dic['TLE']=0
dic['RE']=0

for i in range (N):
    _=input()
    dic[_]+=1

print('AC x {0}'.format(dic['AC']))
print('WA x {0}'.format(dic['WA']))
print('TLE x {0}'.format(dic['TLE']))
print('RE x {0}'.format(dic['RE']))