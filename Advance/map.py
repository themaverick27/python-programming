# Map

numbers = [1, 2, 3, 4]
result = map(lambda x : x**2, numbers)

print(result)
print(list(result))

# other way - normal function, instead of lambda fn
def doubled(x):
    return x**2;

ans = map(doubled, numbers)
print(list(ans))