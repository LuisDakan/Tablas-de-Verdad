
def AND(r,s):
    return r*s

def OR(r,s):
    if(r+s): return 1
    else: return 0

def NOT(r):
    if(r): return 0
    else: return 1

def COND(r,s):
    if(s==0 and r==1):
        return 0
    else:
        return 1

def BICOND(r,s):
    if(r==s): return 1
    else: return 0