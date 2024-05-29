
import Prepare as pp
import Operation as Op
import Solve as sv

def showTable():
    pass

def main():
    prop=input("Ingrese la proposición lógica: ")
    variables=pp.getVar(prop)
    entries=pp.getInputs()
    for i in entries:
        sv.SolExpr()
    showTable()

