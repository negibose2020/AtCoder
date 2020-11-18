a=input()
l=[int(a[0]),int(a[1]),int(a[2]),int(a[3])]

for i in range (2**3):
    op=[]
    for j in range(3):
        if (i>>j) & 1 == 1:
            op.append(+1)
        else:
            op.append(-1)
    # print(op)
    # print('{}{}{}{}{}{}{}'.format(l[0],op[0],l[1],op[1],l[2],op[2],l[3]))
    # print(l)
    # print(op)

    # l[0]+(op[0]*l[1])+(op[1]*l[2])+(op[2]*l[3])==7
    if l[0]+(op[0]*l[1])+(op[1]*l[2])+(op[2]*l[3])==7: 
        options=[]
        for option in op:
            if option ==1:
                options.append('+')
            else:
                options.append("-")
        print('{}{}{}{}{}{}{}=7'.format(l[0],options[0],l[1],options[1],l[2],options[2],l[3]))
        break


# bit全探索