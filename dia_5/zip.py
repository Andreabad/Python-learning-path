nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]

combinado = list(zip(nombres,edades))
print(combinado)


nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinado = list(zip(nombres,edades,ciudades))
print(combinado)



nombres = ['Ana','Hugo','Valeria']
edades = [65,29,42]
ciudades = ['Lima','Madrid','Mexico']

combinado = list(zip(nombres,edades,ciudades))

for nombres,edades,ciudades in combinado:
    print(f"{nombres} tiene {edades} años y vive en {ciudades}")