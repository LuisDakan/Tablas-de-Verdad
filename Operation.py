
def AND(r,s):
    return r*s

def OR(r,s):
    return r+s

def NOT(r):
    return (not r)

def COND(r,s):
    if(s==0 and r==1):
        return 0
    else:
        return 1

def BICOND(r,s):
    return r^s