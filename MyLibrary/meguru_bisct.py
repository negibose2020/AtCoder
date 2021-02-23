def is_ok(condition):
    '''
    okの条件を記載する。
    個別の問題でそれぞれ定義する。
    '''
    
    if  condition==True:
        return True
    else:
        return False

def megru_bisect(ok,ng):
    while(abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok