texto = input("Puedes ingrsar un texto: ")
letras =[]

texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower()) 
letras.append(input("Ingresa la segunda letra: ").lower()) 
letras.append(input("Ingresa la tercera letra: ").lower()) 




# texto = list(texto)
# letras = list(letras)

# cuantas veces se repite cada letra
print("Cantidad de letras")
cantidad_de_letras1 = texto.count(letras[0])
cantidad_de_letras2 = texto.count(letras[1])
cantidad_de_letras3 = texto.count(letras[2])
print(f"La letra '{letras[0]}' repetida {cantidad_de_letras1} veces ")
print(f"La letra '{letras[1]}' repetida {cantidad_de_letras2} veces ")
print(f"La letra '{letras[2]}' repetida {cantidad_de_letras3} veces ")

# cuantas palabras hay en el texto
print("Cantidad de palabras")
palabras = texto.split()

print(f"El texto tiene' {len(palabras)}' palabras")

# informar cual es la primera y ultima letra del texto
print("Letra inicial y letra final")
letra_inicial = texto[0]
letra_final = texto[-1]

print(f"La primera letra del texto es '{letra_inicial}' y la ultima letra del texto es '{letra_final}")


# texto al reves
print("Palabras en orden inverso")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"El texto de manera invertida se veria asi:\n '{texto_invertido}'")

# comprobrar si aparece la palabra python en el texto
print("¿La palabra 'Python' se encuentra en el texto?")

print("python " in texto)


