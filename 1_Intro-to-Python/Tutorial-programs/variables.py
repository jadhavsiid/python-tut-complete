# Creating Variables
a = 10
d = "Joe"
print(a)
print(d)

print(' ')

# Variable names are case sensitive
b = 4
B = "Harry"
print(b)
print(B)
# Above both variables are different and one will not override other.

print(' ')

# Variables automatically adopt to the type of data they hold and can be reassigned to data of any other type
x = 20
print(x)
x = 'Twenty'
print(x)

print(' ')

# Casting is done to specify the data type of a variable
c = str('4')
e = int(40)
f = float('20')
print(c)
print(e)
print(f)

# type() is used to get the actual data type of any variable

print(type(x))
print(type(f))
print(type(a))
print(type(b))
print(type(c))
print(type(d))