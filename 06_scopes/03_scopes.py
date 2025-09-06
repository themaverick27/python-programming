x = 99

def func():
    global x # bad practice, do not use global
    x = 11

func()
print(x)