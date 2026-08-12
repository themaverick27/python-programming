# Qs: Write a Python script to merge two Python dictionaries?
dict1 = {
    "name": "Maverick",
    "age": 29,
    "city": "Pune"
}

dict2 = {
    "course": "Python",
    "language": "English"
}

merge_dict = {}
for k in dict1:
    merge_dict[k] = dict1[k]
for k in dict2:
    merge_dict[k] = dict2[k]

print(merge_dict)


# Qs: Write a Python program to sum all the values in a dictionary?

dict = {
    "first" : 100,
    "second" : 125,
    "third" : 178,
    "fourth" : 454
}

values_sum = 0
for v in dict.values():
    values_sum += v
print(values_sum)

# Qs: Count the frequency of each element

ls = [10, 11, 25, 41, 11, 45, 11, 25, 10, 12]

freq = {}
for i in range(len(ls)):
    key = ls[i]

    if key in freq:
        freq[key] += 1
    else:
        freq[key] = 1

print(freq)

# Qs: Write a Python program to combine two dictionary by adding values for common keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

final_dict = {}
for i in dict1:
    key = i
    sum = dict1[key]
    for j in dict2:
        if i == j:
            sum += dict2[j]
            break

    final_dict[key] = sum

for k in dict2:
    if k not in final_dict:
        final_dict[k] = dict2[k]

print(final_dict)