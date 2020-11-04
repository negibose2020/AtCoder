def determination_of_multiples_of_two(num):
    numToStr=str(num)[-1]
    if int(numToStr)%2==0:
        return True
    else:
        return False

def determination_of_multiples_of_three(num):
    numToStr=str(num)
    judge=0
    for _ in numToStr:
        judge+=int(_)
    if judge%3==0:
        return True
    else:
        return False

def determination_of_multiples_of_four(num):
    numToStr=str(num)
    if len(numToStr)==1:
        numToStr=numToStr.zfill(2)
        # print(int(numToStr))
        
    if int(numToStr[-2:])%4==0:
        return True
    else:
        return False

def determination_of_multiples_of_five(num):
    numToStr=str(num)[-1]
    if int(numToStr)%5==0:
        return True
    else:
        return False

def determination_of_multiples_of_six(num):
    if determination_of_multiples_of_two(num) and determination_of_multiples_of_three(num):
        return True
    else:
        return False

def determination_of_multiples_of_seven(num):
    if int(num)%7==0:
        return True
    else:
        return False

def determination_of_multiples_of_eight(num):
    numToStr=str(num)
    if len(numToStr)==1:
        numToStr=numToStr.zfill(3)
        # print(int(numToStr))
        
    if int(numToStr[-3:])%8==0:
        return True
    else:
        return False

def determination_of_multiples_of_nine(num):
    numToStr=str(num)
    judge=0
    for _ in numToStr:
        judge+=int(_)
    if judge%9==0:
        return True
    else:
        return False

def determination_of_multiples_of_ten(num):
    numToStr=str(num)[-1]
    if int(numToStr)==0:
        return True
    else:
        return False

def determination_of_multiples_of_eleven(num):
    numToStr=str(num)
    judge=0
    for i in range (len(numToStr)):
        if i%2==0:
            judge+=int(numToStr[i])
        else:
            judge-=int(numToStr[i])
    if judge%11==0:
        return True
    else:
        return False

def determination_of_multiples_of_twelve(num):
    if determination_of_multiples_of_three(num) and determination_of_multiples_of_four(num):
        return True
    else:
        return False