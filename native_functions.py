var = "test"

print(len(var))
print(type(var))
print(max(var))
print(min(var))
print(pow(10,2))
print(round(11.6))

# ID returns memory address
print(id(var))

# FORMAT
name_1,name_2="May","Nicolas"
age_1,age_2=12,15
enfants="{} and {} are {} and {} years old respectively.".format(name_1,name_2,age_1,age_2)
print(enfants)

# ISINSTANCE
temp=1.0
print(isinstance(temp, int))
print(isinstance(temp, (int,float)))

# DICT, LIST, TUPLE, SET
my_tuple=tuple((1,2,"three"))
print(type(my_tuple))
print(my_tuple)

# ENUMERATE
import numpy as np
X=np.arange(1,16,2)
print(X)
for i, el in enumerate(X):
    if el > 13:
        print("index:", i, "Element",el)

# MAP
words = ("This", "is", "a", "cat")
mapped = map(str.upper, words)
print(*mapped)

# SORTED
a=range(1,10) 
print(sorted(a))
print(sorted(a, reverse=True))

# REVERSED
print(list(reversed(a)))

# ZIP - bind pairs
names=["Alex","Pierre","Jean"]
ages=[15,14,17]
list_zip=list(zip(names,ages))
print(list_zip)

# COMPILE - compile(source, filename, mode, flag, dont_inherit, optimize)
x = compile('print(55)', 'test', 'eval')
exec(x)

# DIR - Returns a list of the specified object's properties and methods
class Person:
    name = "John"
    age = 36
    country = "Norway"
print(dir(Person))

# GETATTR
person = Person()
print(getattr(person, "name"))

# SETATTR
setattr(person, "status", "free")
print(person.status)

# HASH
print(hash(person))

# ITER
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# ISSUBCLASS
class myAge:
    age = 36
class myObj(myAge):
    name = "John"
    age = myAge
print(issubclass(myObj, myAge))

# ORD CHR
print(ord("🐑"))
print(chr(128017))

# REPR
print(repr(person))