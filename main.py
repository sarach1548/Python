from datetime import datetime
from functools import wraps

def repet(n):
    def decorator(func):
        def wraper(*args, **kwargs):
            firstTime = datetime.now()
            for _ in range(n):
                func(*args, **kwargs)
            print(datetime.now() - firstTime)

        return wraper

    return decorator


@repet(50000)
def one():
    print("func one")


one()

# Ex2
dicCache = dict()

def cache():
    def wrapper(func):
        if dicCache[func] == None:
            dicCache[func]=func
        else:
            return dicCache[func]
    return wrapper

@cache
def f1():
    print("f1")

f1()