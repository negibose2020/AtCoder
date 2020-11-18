# AtCoder Beginner Contest 183
# B - Billiards

Sx,Sy,Gx,Gy=map(int,input().split())
Gy=(-1)*Gy

ans=((Gx-Sx)*(0-Sy)/(Gy-Sy))+Sx
print(ans)

'''
xy平面状のS(Sx,Sy)とG(Gx,Gy)を通る直線を二次関数として表すと、
(Gx-Sx)(y-Sy)=(Gy-Sy)(x-Sx)
y=0の場合のxの値を知りたいので、yに0を代入し、xについて解くと上記の式になる。
'''