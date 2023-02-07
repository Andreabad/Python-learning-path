# integer aleatorio
from random import randint

aleatorio = randint(1,50)
print(aleatorio)

# valor aleatorio pero decimal dentro del rango
from random import *

# aleatorio = uniform(1,5)

# numero decimal corto
aleatorio = round(uniform(1,5),1)
print(aleatorio)

# aleatorio
# siempre te va a dar una fraccion de un numero entero
from random import *

aleatorio = random()
print(aleatorio)

# choice te permite trabajar con una seleccion aleatoria dentro de los elementos de una lista
from random import *

colores = ['azul','rojo','verde','amarillo']
aleatorio = choice(colores)
print(aleatorio)

# shuffle quiere decir mezclar 
# shuffle no se puede almacenar en una lista
# no se puede usar con strings ya que son inmutables
from random import *

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)