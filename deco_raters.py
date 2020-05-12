def do_something(func):
    def wrapper():
        print("This is first")
        func()
        print("This is last")
    return wrapper

@do_something
def print_something():
    print("Hello")


print_something()