import Prepare as pp
import Operation as Op
import Solve as sv

def code(char):
    if char=='¬':
        return '$\\neg$'
    elif char=='→':
        return '$\\rightarrow$'
    elif char=='v':
        return '$\\lor$'
    elif char=='∧':
        return '$\\land$'
    elif char=='↔':
        return '$\\leftrightarrows$'
    else: return char

def showTable(prop,variables,entries,results,clase):
    columns=len(variables)
    for i in range(len(prop)):
        if(prop[i]!='(' and prop[i]!=')'):
            columns+=1
    ind='    '
    lengthV=len(variables)
    cad=ind+'''\\begin{table}[h]
        \caption{Tabla de verdad}\n        \\centering
        \\begin{tabular}{'''
    for i in range(columns):
        cad+="|c"
    cad+="|}\n"+ind+ind+ind+'\\hline \n'
    cad+=ind+ind+ind+'\\multicolumn{'+str(lengthV)+'}'+'{ |c }{'
    for i in variables:
        cad+=i+' '
    cad+='} & \n'
    cad+=ind+ind+ind+'\\multicolumn{'+str(columns-lengthV)+'}'+'{ |c|}{'
    for i in range(len(prop)-1):
        if(prop[i]!='(' and prop[i+1]!=')'):
            cad+=code(prop[i])+' '
        else: cad+=code(prop[i])
    cad+=prop[-1]+'} \\\\'+'   \\hline \n'
    for i in range(len(entries)):
        cad+=ind+ind+ind
        for j in entries[i]:
            cad+=str(j)+' & '
        for j in range(len(prop)-1):
            if(prop[j]!='(' and prop[j]!=')'):
                if(prop[j+1]==')'):
                    cad+=str(results[i][j])
                else: cad+=str(results[i][j])+' & '
        if(prop[-1]!=')'): cad+=str(results[i][-1])
        cad+='\\\\   \\hline  \n'
    cad+=ind+ind+'\\end{tabular}\n'
    cad+=ind+'\\end{table}\nEs una '
    if(clase==len(entries)):
        cad+='Tautología '
    elif (clase):
        cad+='Contingencia'
    else:
        cad+='Contradiccion'
    with open("TablaL.txt","w",encoding="utf-8") as ap:
        ap.write(cad)
    

def main():
    prop=input("Ingrese la proposición lógica (→ v ∧ ↔ ¬): ") 
    results=[]
    variables=pp.getVar(prop)
    dictio={}
    for i in variables:
        dictio[i]=-1
    entries=pp.getInputs(len(variables))
    clase=0
    for i in entries:
        l=[]
        clase+=sv.SolExpr(entry=i,dictio=dictio,variables=variables,prop=prop,l=l)
        results.append(l)
    showTable(prop=prop,variables=variables,entries=entries,results=results,clase=clase)

main()