
def evaluate(sol,l,r):
    for i in range(l,r):
        pass


def separate(sol,l,r):
    stack=[]
    for i in range(l,r):
        if(sol[i]==')'):
            separate(sol,stack[-1],i)
        elif (sol[i]=='('):
            stack.append(i)
    evaluate(sol,l,r)

def SolExpr(entry,dictio,variables,prop):
    for i in range(len(entry)):
        dictio[variables[i]]=entry[i]
    l=[]
    i=0
    for i in dictio:
        if(i in dictio):
            l.append(dictio[i])
        else:
            l.append(i)

    