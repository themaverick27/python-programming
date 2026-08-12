# List methods 

# print(dir(list)) 
# help(list)

numbers = [10, 20, 30, 40, 50]
print(numbers)

# append method
numbers.append(100)
numbers.append(120)
print(numbers)

# insert method
numbers.insert(1, 450)
print(numbers)

# extend method
numbers.extend([450, 9, 99, 999])
print(numbers)

# remove method - remove first occurrence of value
numbers.remove(450)
print(numbers)

# pop method 
numbers.pop()
print(numbers)

# index method
index = numbers.index(50)
print(index)

# count method
count = numbers.count(450)
print(count)

# sort the list
numbers.sort()
print(numbers)

# reverse the list
numbers.reverse()
print(numbers)

# copy method - return a shallow copy of list
new_list = numbers.copy()
print(new_list)

# clear method
numbers.clear()
print(numbers)