x = 99
def func1():
    x = 88
    def func2():/
        print(x)
    #return func2() # this the execution of function2 and then returning
    return func2 # this will return the reference of function2

result = func1()
print(result) # prints the reference 
result() # execute the function stored

# this is what we called as closures