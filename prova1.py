# Nathan Zurita Barreto
# 202414358

#1º Qustão:

def numeros(a, b, c):
    if a == b == c:
        return 3
    elif a == b or a == c or b == c:
        return 2
    else:
        return 0


resultado1 = numeros(8,8,8)
resultado2 = numeros(4,4,7)
resultado3 = numeros(0,1,2)

print(resultado1)
print(resultado2)
print(resultado3,)
print("----------")


#2º Questão:
def triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a
print(triangulo(7,8,9))
print(triangulo(4,5,6))
print(triangulo(1,2,3))
print("----------")

#3º Questão:

def tipo_do_triangulo(a, b, c):
    if not triangulo(a,b,c):
        return "Isso n vai formar triângulo👍"
    parecidos = numeros(a,b,c)
    if parecidos == 3:
        return "Equilátero"
    elif parecidos == 2:
        return "Isósceles"
    elif parecidos == 1:
        return "Escaleno"

print(tipo_do_triangulo(9,9,9))
print(tipo_do_triangulo(9,10,10))
print(tipo_do_triangulo(9,10,11))