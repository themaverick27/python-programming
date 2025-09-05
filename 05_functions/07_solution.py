# Problem: Write a function that takes variable number of arguments and returns their sum. (Function with *args)

def sum_all(*args):
    print(args)

    ans = 0
    for i in args:
        ans += i
    return ans
    
    # return sum(args) # finding sum using built-in method sum()


print(sum_all(1, 2))
print(sum_all(1, 4, 7, 11, 12))