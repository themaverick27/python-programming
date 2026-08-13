# Args and Kwargs

def addition(a, b):
    return a+b

print(addition(4, 5))
#print(addition(5, 7, 8)) # error

def multiply(*args):
    #print(args) # tuple
    ans = 1
    for i in args:
        ans *= i
    print(ans)


# any number of arguments can be passed now, due to args (used for capturing multiple arguments)
multiply(4, 5)
multiply(4, 5, 6, 7)
multiply(2, 7, 10) 