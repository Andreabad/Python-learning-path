def multiplicar(numero1,numero2):
    return numero1 * numero2

resultado = multiplicar(5,10)
print(resultado)

# tambien pueden tener la operacion o codigo dentro variables internas
def multiplicar(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar(5,10)
print(resultado)


# practicas
# 1
def potencia(base,exponente):
    return base ** exponente

resultado= potencia(3,4)
print(resultado)

# 2
def usd_a_eur(dolar):
    return dolar * 0.90
dolares = usd_a_eur(1)
print(dolares)

# 3
def invertir_palabra(palabra):
    return palabra[::-1].upper()

palabra = "Python"
resultado = invertir_palabra(palabra)
print(resultado)

