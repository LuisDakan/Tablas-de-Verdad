
import Prepare as pp
import Operation as Op
import Solve as sv

def showTable(prop,variables,entries,results=[]):
    for i in variables:
        print(i,end=" ")
    print(" | ",end="")
    for i in range(len(prop)):
        if(i<len(prop)-1 and (prop[i+1]!='>' and (prop[i]!='<'))):
           print(prop[i],end=" ")
        else: print(prop[i],end="")
    print()
    for i in range(2*(len(variables)+len(prop)+3)):
        print("-",end="")
    print()
    for i in entries:
        for j in i:
            print(j,end=" ")
        print()

def main():
    prop=input("Ingrese la proposición lógica: ")
    variables=pp.getVar(prop)
    #print(variables)
    entries=pp.getInputs(len(variables))
    for i in entries:
        sv.SolExpr(i)
    showTable(prop=prop,variables=variables,entries=entries)

main()