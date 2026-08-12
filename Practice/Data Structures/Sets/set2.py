# Operations on Two Sets - union, intersection, difference, symmetric difference

a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 7, 8, 9, 10}

# union_set = a.union(b)
union_set = a | b
print(union_set)

# intersection_set = a.intersection(b)
intersection_set = a & b
print(intersection_set)

# difference_set = a.difference(b)
difference_set = a - b
print(difference_set)

# difference_set = b.difference(a)
difference_set = b - a
print(difference_set)

# symmetric_diff = a.symmetric_difference(b)
symmetric_diff = a ^ b
print(symmetric_diff)