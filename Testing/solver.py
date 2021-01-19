def add(a, b):
    res=a+b
    print (f"{a}+{b}={res}")
    return res


def square_equation_solver(a,b,c):
    if not all(map(lambda p: isinstance(p,(int,float)),(a,b,c))):
        raise TypeError("Not valid type")
    print("Types are OK")