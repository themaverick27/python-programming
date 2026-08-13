# kwargs (keyword arguments)

def addition(**kw):
    #print(kw) # dictionary
    sum = 0
    for i in kw.values():
        sum += i
    print(sum)


addition(a = 12, b = 14, c = 16)
addition(x = 22, y = -14, z = -16)


def information(**kwargs):
    print("Information: ")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")


information(name = "tom", show = "jerry", year = 1980)