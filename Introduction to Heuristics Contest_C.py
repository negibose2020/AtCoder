from operator import mul

# D=int(input())
# clist=list(map(int,input().split()))
# slist=[]
# for i in range (D):
#     s=list(map(int,input().split()))
#     slist.append(s)
# tlist=[]
# for i in range(D):
#     t=int(input())
#     tlist.append(t)
# changelist=[]
# D2=int(input())
# for i in range (D2):
#     change=list(map(int,input().split()))
#     changelist.append(change)

D=5
clist=[86, 90, 69, 51, 2, 96, 71, 47, 88, 34, 45, 46, 89, 34, 31, 38, 97, 84, 41, 80, 14, 4, 50, 83, 7, 82]
slist=[[19771, 12979, 18912, 10432, 10544, 12928, 13403, 3047, 10527, 9740, 8100, 92, 2856, 14730, 1396, 15905, 6534, 4650, 11469, 3628, 8433, 2994, 10899, 16396, 18355, 11424], [6674, 17707, 13855, 16407, 12232, 2886, 11908, 1705, 5000, 1537, 10440, 10711, 4917, 10770, 17272, 15364, 19277, 18094, 3929, 3705, 7169, 6159, 18683, 15410, 9092, 4570], [6878, 4239, 19925, 1799, 375, 9563, 3445, 5658, 19857, 11401, 6997, 6498, 19933, 3848, 2426, 2146, 19745, 16880, 17773, 18359, 3921, 14172, 16730, 11157, 5439, 256], [8633, 15862, 15303, 10749, 18499, 7792, 10317, 5901, 9395, 11433, 3514, 3959, 5202, 19850, 19469, 9790, 5653, 784, 18500, 10552, 17975, 16615, 7852, 197, 8471, 7452], [19855, 17918, 7990, 10572, 4333, 438, 9140, 9104, 12622, 4985, 12319, 4028, 19922, 12132, 16259, 17476, 2976, 547, 19195, 19830, 16285, 4806, 4471, 9457, 2864, 2192]]
tlist=[1, 17, 13, 14, 13]
D2=5
changelist=[[1, 7], [4, 11], [3, 4], [5, 24], [4, 19]]

benefitlist=[0]*(D+1)
noheldsdaylist=[[0]*26 for i in [1]*(D+1)]

for j in range (D2):
    tlist[changelist[j][0]-1]=changelist[j][1]
    
    for i in range (changelist[j][0],D+1):
        _benefitlist=benefitlist[:changelist[j][0]]
        _noheldsday=noheldsdaylist[:changelist[j][0]]
        _noheldsday_today=list(map(lambda x: x+1,_noheldsday[i]))
        _noheldsday_today[tlist[i]-1]=0
        noheldsdaylist[i]=_noheldsday_today

        # _noheldsday=list(map(lambda x: x+1,replace_day))
        _noheldsday[tlist[i]-1]=0
        unpleasant=list(map(mul,clist,_noheldsday))
        v=slist[i][tlist[i]-1]-sum(unpleasant)
        _benefitlist.append(v)

    noheldsday=_noheldsday
    benefitlist=_benefitlist
    print(sum(_benefitlist))