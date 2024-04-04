def my_function() :
    print('Hello!')

my_function()

val = my_function()
print(val)

def my_function2(foo, bar = 0) :  #0 es valor por defecto
    print(foo)
    print(bar)
    return "Hi, i'm David"

my_function2(50,60)

my_function2(bar = 10, foo =20) #cambiar orden definiendo el valor de cada variable

my_function2(foo = 30)  

def my_function3() :
    var = 100
    print(var)

my_function3()

# print(var)   // esto genera error porque solo se define var dentro de la funcion

var2 = 1000

def my_function4() :
    
    print(var2)

my_function4() # En este caso si que se imprime porque var2 es variable global