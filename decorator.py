def decorator(func):
    def wrap(*args,**kwargs):
        result = func(*args,**kwargs)
        return result * 2
    return wrap

@decorator
def add(a,b):
    return a+b

print(add(2,3))

