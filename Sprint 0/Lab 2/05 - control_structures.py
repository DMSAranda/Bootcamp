foo = 15

if foo > 20 :
    print(foo)

elif foo < 20 and foo > 10 :
    print("in the middle!")
else :
    print("not good!")


foo2 = 12

if isinstance(foo2, int) :
    if foo2 > 10 :
        print(foo2)


foo3 = [1,2,3,4,5]

for var in foo3 :
    print(var)



foo4 = {"a":100, "b":200, "c":300}

for var in foo4.values() :
    print(var)

for var2 in foo4.keys() :
    print(var2)

for key, val in foo4.items() :
    print(key)
    print(val)

for value in range(10) : 
    print(value)


foo5 = [value for value in range(100)]

print(foo5)