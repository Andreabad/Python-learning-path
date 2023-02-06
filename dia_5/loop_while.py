# monedas = 5

# while monedas > 0:
#     print(f"tengo {monedas} monedas")
#     # monedas = monedas - 1
#     monedas -= 1
# else:print("No tengo mas dinero")

# respuesta = 's'

# while respuesta == 's':
#     respuesta = input("Quieres seguir? (s/n)")
# else:
#     print("Gracias")


# respuesta = 's'

# while respuesta == 's':
#     pass
# # tiquet para guardar un espacio para el programador

# print("hola")

# nombre = input("Tu nombre: ")

# for letra in nombre:
#     if letra == 'r':
#         break
#     # interrumpir
#     print(letra)

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'r':
        continue
    # se interrumpe antes de llegar al print y continua con las siguientes
    print(letra)