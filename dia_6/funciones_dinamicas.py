def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)

def chequear_3_cifras(numero):
    return numero in range(100,1000)

suma = 586 + 402

resultado = chequear_3_cifras(suma)
print(resultado)


# veridifique todos los elementos de una lista


def chequear_3_cifras(lista):
    
    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

resultado = chequear_3_cifras([555,99,600])
print(resultado)


def chequear_3_cifras(lista):
    
    lista_3_cifras = []
    
    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    return lista_3_cifras

resultado = chequear_3_cifras([555,99,600])
print(resultado)



# practica
# 1
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
    return True

lista_numeros = [1,5,-9,8]

# 2
def suma_menores(lista_numeros):
    resultado = 0
    for numero in lista_numeros:
        if 0 < numero < 1000:
            resultado += numero
    return resultado

lista_numeros = [10,5000,800,60,2000]

# 3
def cantidad_pares(lista_numeros):
    resultado = 0
    for n in lista_numeros:
        if n % 2 == 0:
            resultado += 1
    return resultado

lista_numeros = [1,3,8,10,9,20,25]



