"""
decorator test
"""

def make_pretty(func):
    def inner():
        print("i got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinatory")

ordinary()

def decorator(func):
    def wrapper():
        print("first")
        func()
        print("second")
    return wrapper

@decorator
def say_hello():
    print("hello")

say_hello()