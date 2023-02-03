# frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
# eliminado = frutas.pop(1)
# print(frutas)
# print(eliminado)

# dic = {'c1':['a','b','c'],'c2':['d','e','f']}
# print(dic['c2'][1].upper())

# mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}


# mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
# print(mi_dict["puntos"]['points2'][1])
# print(dic['c2'][1])

# mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
# mi_dic["edad"] = 36
# mi_dic["ocupacion"] = "Editora"
# mi_dic["pais"] = "Colombia"
# print(mi_dic)

# numero = 25**0.5 == 25
# print(numero)

# num1 = 64 * 3
# num2 = 24 * 8
# mi_bool = num1!=num2


# num1 = input("Ingresa un número:")
# num2 = input("Ingresa otro número:")
# if num1>num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2>num1:
#     print(f"{num2} es mayor que {num1}")
# elif num1==num2:
#     print(f"{num1} es igual que {num2}")

# edad = 16
# calificacion = 9
# if edad <18:
#     print("Eres menor de edad")
#     if calificacion >= 7:
#         print("Aprobador")
#     else:
#         print("No aprobaste")
# else:
#     print("Eres adulto")
    
# edad = 18
# tiene_licencia = False

# tienes mas 18 y tienes licencia?
# en caso contrario "No puedes conducir aún. Debes tener 18 años y contar con una licencia"
# tienes una licencia?

# if edad>18 and tiene_licencia == True:
#     print("Puedes conducir")
# else:
#     print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")

# if  not tiene_licencia:
#     print("No puedes conducir. Necesitas contar con una licencia") 
    
# habla_ingles = True
# sabe_python = False
# if habla_ingles == True and sabe_python == False:
#     print("Para postularte, necesitas saber programar en Python")

# lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
# suma_numeros = 0

# for numero in lista_numeros:
#     suma_numeros = suma_numeros + numero
# print(suma_numeros)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    resto = numero % 2
    if resto == 0:
        suma_pares += numero
    else:
        suma_impares += numero
print(suma_pares)
print(suma_impares)


numero = 7
suma_pares = 0
suma_impares = 0
resto = numero % 2
if resto == 0:
    suma_pares += numero 
else:
    suma_impares += numero
print(suma_pares)
print(suma_impares)
