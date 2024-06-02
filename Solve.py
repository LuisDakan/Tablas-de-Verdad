import Operation as Op

def negate(index,sol):
    if(sol[index]!='¬'):
        return index
    sol[index]=Op.NOT(sol[negate(index+1,sol)])
    return index

def evaluate(sol,l,r,dictio):
    final=l
    i=l
    while i<r:
        if(sol[i]=='¬'):
            negate(i,sol)
            if((i+1) in dictio):
                i=dictio[i+1]
        i+=1
    i=l
    while i<r:
        if(type(sol[i])==str):
            if(sol[i]=='v'):
                sol[i]=Op.OR(sol[final],sol[i+1])
            if(sol[i]=='∧'):
                sol[i]=Op.AND(sol[final],sol[i+1])
            if(sol[i]=='→'):
                sol[i]=Op.COND(sol[final],sol[i+1])
            if(sol[i]=='↔'):
                sol[i]=Op.BICOND(sol[final],sol[i+1])
            final=i
            if((i+1) in dictio):
                i=dictio[i+1]
        i+=1
    #print(final)
    return final

def separate(sol,l,r):
    stack=[]
    dictio={}
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
    #aux=separate(l,0,len(l))
    #print(aux)
    return l[separate(l,0,len(l))]

    