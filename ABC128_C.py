def AreAllTheLightsOn(SwitchPattern,M,LineVolume,Destinations,p):
    # print(SwitchPattern)
    Light=0
    for m in range(M):
        OnSwitch=0
        for l in range(LineVolume[m]):
            a=Destinations[m][l]-1
            if SwitchPattern[a]==1:
                OnSwitch += 1
            else:
                pass
        if OnSwitch%2==p[m]:
            Light+=1
    # print (Light)
    if Light==M:
        return True


N,M=map(int,input().split())
K=[]
for _a in range (M):
    arr=list(map(int,input().split()))
    K.append(arr)
LineVolume=[] #m番目の電球がスイッチとつながっている線の数
Destinations=[] #m番目の電球がつながっているスイッチの番号(1スタート)
for _b in range (M):
    LineVolume.append(K[_b][0])
    Destinations.append(K[_b][1:])
p=list(map(int,input().split()))
# print (LineVolume)
# print (Destinations)
# print(p)

LightOnPattern=0
#bit全探索
for Pattern in range (2**N):
    SwitchPattern=[]
    for ONOFF in range(N):
        if(Pattern>>ONOFF)&1==1:
            SwitchPattern.append(1)
        else:
            SwitchPattern.append(0)
    # print(SwitchPattern)
    if AreAllTheLightsOn(SwitchPattern,M,LineVolume,Destinations,p)==True:
        LightOnPattern += 1

print(LightOnPattern)
