import Operation as Op

def evaluate(sol,l,r,dictio):
    final=0
    i=l
    while i<r:
        if(sol[i]=='¬'):
            final=i
            sol[i]=Op.NOT(sol[i+1])
            if((i+1) in dictio):
                i=dictio[i+1]
        i+=1
    i=l
    while i<r:
        if(type(sol[i])==str):
            final=i
            if(sol[i]=='v'):
                sol[i]=Op.OR(sol[i-1],sol[i+1])
            if(sol[i]=='∧'):
                sol[i]=Op.AND(sol[i-1],sol[i+1])
            if(sol[i]=='→'):
                sol[i]=Op.COND(sol[i-1],sol[i+1])
            if(sol[i]=='↔'):
                sol[i]=Op.BICOND(sol[i-1],sol[i+1])
            if((i+1) in dictio):
                i=dictio[i+1]
        i+=1
    return final

def separate(sol,l,r):
    stack=[]
    dictio={}
    follow=[i for i in range(len(sol))]
    for i in range(l,r):
        if(sol[i]==')'):
            izq=stack.pop()
            dictio[izq]=i
            final=separate(sol,izq+1,i)
            sol[izq]=sol[final]
            sol[i]=sol[final]
        elif (sol[i]=='('): 
            stack.append(i)
    return evaluate(sol,l,r,dictio)

def SolExpr(entry,dictio,variables,prop,l):
    for i in range(len(entry)):
        dictio[variables[i]]=entry[i]
    i=0
    for i in prop:
        if(i in dictio):
            l.append(dictio[i])
        else:
            l.append(i)
    return l[separate(l,0,len(l))]

    