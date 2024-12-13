import numpy as np
from itertools import combinations

def modelos_triângulos(lados):
    escaleno = 0
    isosceles = 0
    equilatero = 0
    
    combinações = list(combinations(lados, 3))

    for a,b,c in combinações:
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                equilatero += 1
            elif a == b or b == c or a == c:
                isosceles += 1
            else:
                escaleno += 1
    return escaleno, isosceles, equilatero

lados = np.array([3,4,5,4,6,4,10,16])
resultado = modelos_triângulos(lados)
print(resultado)