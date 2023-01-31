nombre = input("¿Cual es tu nombre?: ")
ventas = input("¿Cuanto has vendido?: ")
ventas = int(ventas)
comision = ventas *13/100
comision =round(comision,2)
print(nombre, f" la comision por tu ventas es {comision}")
print(f"{nombre}, la comision por tu ventas es {comision}")