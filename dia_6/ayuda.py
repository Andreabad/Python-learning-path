# metodo popitem() se utiliza para eliminar un elemento aleatorio de un diccionario
dic = {'clave1': 100,'clave2': 500}

a = dic.popitem()
print(a)
print(dic)

# pratica
# 1: metodo lstrip()El siguiente código en Python imprimirá el resultado de aplicar el método lstrip() a la cadena proporcionada:
string =",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
a = string.lstrip(",:%_#")
print(a)
# 2: metodo insert() insertar un elemento en una lista en una posición específica
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)

# 3 metodo isdisjoint() utiliza para verificar si dos conjuntos no tienen elementos en común
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)