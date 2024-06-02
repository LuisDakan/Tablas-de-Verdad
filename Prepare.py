import re

def getVar(prop):
    Svariables=set()
    for x in prop:
        if(re.match("[a-z]",x) and x!='v'):
            Svariables.add(x)
    return sorted(Svariables)

def getInputs(n):
    l=[]
    for i in range(1<<n):
        m=[]
        for j in range(n):
            if((1<<j)&i): m.insert(0,1)
            else: m.insert(0,0)
        l.append(m)
    return l

import re

def es_sintaxis_correcta(proposicion):
    # Expresión regular para reconocer variables, operadores lógicos y paréntesis
    patron = re.compile(r'^[()\sA-Za-z01→v∧↔¬]+$')
    
    # Verificar que solo contenga caracteres permitidos
    if not patron.match(proposicion):
        return False
    
    # Verificar balanceo de paréntesis
    balanceo = 0
    for char in proposicion:
        if char == '(':
            balanceo += 1
        elif char == ')':
            balanceo -= 1
        if balanceo < 0:
            return False
    
    if balanceo != 0:
        return False
    
    # Verificar estructura de operadores y operandos
    tokens = re.findall(r'[A-Za-z01]+|[→v∧↔¬()]', proposicion)
    if not tokens:
        return False
    
    ultimo_token = None
    for token in tokens:
        if token == '(':
            if ultimo_token and ultimo_token not in '→v∧↔¬(':
                return False
            ultimo_token = token
        elif token == ')':
            if ultimo_token in '→v∧↔¬(' or ultimo_token is None:
                return False
            ultimo_token = token
        elif token in '→v∧↔':
            if ultimo_token in '→v∧↔¬' or (not(ultimo_token is None) and ultimo_token not in '('):
                return False
            ultimo_token = token
        elif token == '¬':
            if not(ultimo_token is None) and ultimo_token not in '('  and ultimo_token not in '→v∧↔':
                return False
            ultimo_token = token
        else:  # Es un operando (variable o constante)
            if not(ultimo_token is None) and ultimo_token not in '(' and ultimo_token not in '→v∧↔¬':
                return False
            ultimo_token = token
    
    if ultimo_token in '→v∧↔¬':
        return False
    
    return True







