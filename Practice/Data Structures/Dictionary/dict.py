# Dictionary Concepts - key value pairs, keys must be unique, values can be duplicates

dict = {1: "Hello", 2: "Greet"}
print(dict)

# can modify values - mutable
dict[2] = "Hey"
print(dict)

# access values through keys, instead of index
print(dict[1])

d = {1:"apple", 2:"banana", 3:"citrus", 4:"guava", 5:"kiwi", 6:"mango"}
print(d)
print(d[2])

# add a key-value pair
d.update({7:"orange"})
print(d)

# or 
d[8] = "pineapple" # if key exists, update the value and if not, add this key value pair to dictionary
print(d)

# remove key-value pair
del d[1]
print(d)

# traversing dictionary 
for k in d:
    print(k) # keys
    print(d[k]) # values

for v in d.values():
    print(v)

for k in d.keys():
    print(k)


# dictionary methods

# copy() method - returns a shallow copy of dictionary
d_copy = d.copy()
print(d_copy)

d_copy[2] = "Litchi"
print(d_copy)
print(d)


# items()
print(d.items())

# clear() method - remove all the elements of dictionary
d.clear()
print(d)