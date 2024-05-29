import re

def getVar(prop):
    Svariables=set()
    for x in prop:
        if(re.match("[a-z]",x)):
            Svariables.add(x)
    return sorted(Svariables)

def getInputs(n):
    l=[]
    for i in range(1<<n):
        m=[]
        for j in range(n):
            if((1<<j)&i): m.append(1)
            else: m.append(0)
        l.append(m)
    return l

