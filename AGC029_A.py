N=input()
if N.count('BW')==0:
    print(0)
    exit

count=0
temp_count=1

while temp_count!=0:
    count+=N.count('BW')
    newN=N.replace('BW','WB')
    temp_count=newN.count('BW')
    N=newN

print(count)
