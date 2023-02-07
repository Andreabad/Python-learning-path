import random



nombre = input('Escribe tu nombre: ')
numero_secreto = random.randint(1, 100)
intentos = 0
print(numero_secreto)


print(f"{nombre} He pensado un numero entre el 1 y el 100 y tienes solo 8 intentos para adivinar ")


while intentos <= 8:
    numero = int(input('¿Cual crees que es el numero?: '))
    intentos +=1
    if numero < 1 or numero > 100:
        print("El numero no es valido")
    elif numero < numero_secreto:
        print("la respuesta es incorrecta, el numero es menor al numero secreto")
    elif numero > numero_secreto:
        print("la respuesta es incorrecta, el numero es mayor al numero secreto")
    elif numero == numero_secreto:
        print(f"Has ganado!! te ha tomado {intentos} intentos")
        break
    if intentos == 0:
        print("Lamentablemente no has ingresado un número dentro del rango en los 8 intentos.")
    
    
    





# acerto con el numero secreto
# decirle que gano y cuantos intentos le ha tomado

# si gasto todos los intentos decir gamer over y volver a iniciar

# intentos = 0
# rango = [5, 10]

# while intentos < 8:
#     numero = int(input("Ingrese un número: "))
#     intentos += 1
    
#     if numero >= rango[0] and numero <= rango[1]:
#         print("El número está dentro del rango!")
#         break
#     else:
#         print("El número no está dentro del rango.")

# if intentos == 8:
#     print("Lamentablemente no has ingresado un número dentro del rango en los 8 intentos.")

