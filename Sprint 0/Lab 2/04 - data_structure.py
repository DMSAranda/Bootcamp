foo = [1,2,3]

foo2 = [1, "2", True, [4,5,6]]

print(foo[2])

print(foo[1])

print(foo[-1]) #final de la lista igual que java

print(foo2[-1][2]) #lista dentro de la lista

print(foo2[-1] + foo) #union de listas

print(foo2.append(False))

print(foo2)

print(foo.pop(-1)) #imprime el valor que extrae

print(foo) #imprime como queda el array al sacar el valor con pop

# DICCIONARIO -> similar a Map en Java // clave : valor

foo3 = {"a": 1, "b": 2, "c": 3}

print(foo3)

print(type(foo3))

print(foo3['a'])

foo3.update({"d": 4})

print(foo3)

print(foo3.keys())
print(foo3.values())

