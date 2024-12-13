a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

def gay():
    if a + b > c:
        return(gay)
    elif a + c > b:
        return(gay)
    elif b + c > a:
        return(gay)