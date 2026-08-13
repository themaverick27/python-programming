# Filter

numbers = [1, 2, 3, 4, 5]
even_num = filter(lambda x : x%2 == 0, numbers)

print(even_num)
print(list(even_num))

# other way - normal function, instead of lambda fn
def check_even(x):
    return x%2 == 0

evens = filter(check_even, numbers)
print(list(evens))