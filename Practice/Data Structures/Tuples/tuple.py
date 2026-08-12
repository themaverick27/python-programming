# Tuple Concepts - immutable

tup = (1, 4, 7, 10, 11, 11, 12)
print(tup)

# cannot modify the values of tuple - immutable
#tup[0] = 54
#print(tup)

# access values - indexing
print(tup[0])
print(tup[4])

# travese tuple - 1. using index
for i in range(len(tup)):
    print(tup[i])

# traverse tuple - 2. directly access values
for x in tup:
    print(x)

# tuple methods: 2 methods only
index = tup.index(11)
print(index)

freq = tup.count(11)
print(freq)

# tuple unpacking - unpacking the tuple into variables
a, b, c, d = (1, 2, 3, 4)
print(a)
print(b) 
print(c)
print(d)

x = (5)
print(type(x)) # int, not tuple - because of unpacking

# if you don't want unpacking, use: comma after value
y = (5,)
print(type(y)) # tuple