
import Prepare as pp
import Operation as Op
import Solve as sv

def showTable(prop,variables,entries,results=[]):
    for i in variables:
        print(i,end=" ")
    print(" | ",end="")
    for i in range(len(prop)):
           print(prop[i],end=" ")
    print()
    for i in range(2*(len(variables)+len(prop)+3)):
        print("-",end="")
    print()
    for i in entries:
        for j in i:
            print(j,end=" ")
        print()

def main():
    prop=input("Ingrese la proposición lógica (→ v ∧ ↔ ¬): ")
    results=[]
    variables=pp.getVar(prop)
    dictio={}
    for i in variables:
        dictio[i]=-1
    entries=pp.getInputs(len(variables))
    for i in entries:
        print(sv.SolExpr(entry=i,dictio=dictio,variables=variables,prop=prop))
    #showTable(prop=prop,variables=variables,entries=entries)

main()