def deco(func):
    def wrapper(args):
        for i in args:
            #print(i)
            yield i
    return wrapper

@deco
def print_num(args):
    print("hi")

args = [1,2,3]
gen = print_num(args)
for value in gen:
    print(value)