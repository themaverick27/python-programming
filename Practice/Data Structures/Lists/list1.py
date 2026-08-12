# List Concepts - mutable

ls = [10, 20, 30, True, 45.5, "Dynamic"]
print(ls)

# accessing values - indexing
print(ls[0])
print(ls[4])

# modify value in a list - mutable property
ls[2] = 100
print(ls)

# part of list - slicing
print(ls[0:5:1])

# iterate over list - 1. using index 
for i in range(len(ls)):
    print(ls[i])

# iterate over list - 2. directly on list values 
for x in ls:
    print(x)
