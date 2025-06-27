# decorators  extend function of another func

def add_sprinkles(func):
    def wrapper(*args , **kwargs):
        print("adding sprinkles")
        func(*args , **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args , **kwargs):
        print("add fudge")
        func(*args , **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice(flavor):
    print(f"get icecream flavor {flavor} good")

get_ice("vanilla")