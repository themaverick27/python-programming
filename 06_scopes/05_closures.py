def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

res = chaicoder(2)

print(res) # reference of the actual function

print(res(3)) # execute it and pass the value (x) as 3 (say eg)

# res(3) -> return 3 ** 2 = 9
# prints(res(3)) -> 3