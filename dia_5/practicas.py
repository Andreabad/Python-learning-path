numero = 10
while numero >= 0:
    print(numero)
    numero -= 1
    
    

numero = 50

while numero >= 0:
    resto = numero % 5
    if resto ==0:
        print(numero)
    numero -=1
    
    
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for numero in lista_numeros:
    if numero == -1:
        break
    print(numero)
    
mi_lista = list(range(3,301,3))
print(mi_lista)

suma_cuadrados = 0
for i in range(1,16):
    resto = suma_cuadrados % 2
    if resto== 0:
        print(suma_cuadrados)
     
# practiga rango 3
suma_cuadrados = 0
for i in range(1,16):
   cuadrado = i*i
   suma_cuadrados += cuadrado
print(suma_cuadrados)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
# for count,item in enumerate(lista_nombres):
for indice,item in enumerate(lista_nombres):
    print(f'{item} se encuentra en el índice {indice}')
    
    
lista = ["P","y","t","h","o","n"]
lista_indices = list(enumerate(lista))
print(lista_indices)


lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre[0] == "M":
        print(indice)
        
# zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combinado = list(zip(capitales,paises))

for capitales,paises in combinado:
    print(f"La capital de {paises} es {capitales}")
    


marcas = ['Eucerin','Mondelez','Revolution']
productos = ['Crema','Galleta','Maquillaje']
mi_zip= zip(marcas,productos)
print(mi_zip)

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portugues = ["um", "dois", "três", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espanol,portugues,ingles))
print(numeros)

# minimo y maximo

lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)
print(valor_maximo)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
maximo = max(lista_numeros)
minimo = min(lista_numeros)
rango = maximo - minimo
print(rango)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades())
print(edad_minima)