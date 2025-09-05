# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value. (Function with **kwargs)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name = "racing", movie = "f1", cast = "brad pitt")
print_kwargs(name = "gravity", movie = "interstellar")
print_kwargs(movie = "roman")