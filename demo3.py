class D:
    def __init__(self):
        print('D __init__')

    def __set_name__(self, owner, name):
        print("__set_name__")
        self.name = f"_{name}"

    def __get__(self, inst, owner=None):
        print('__get__')
        return getattr(inst, self.name, 42.0)

    def __set__(self, inst, val):
        print(f"__set__ {val=}")
        setattr(inst, self.name, val)

    def __delete__(self, inst):
        print('__delete__')
        delattr(inst, self.name)

print("---")

class C2():
    d = D()

    def __init__(self):
        self.__dict__['d'] = 2.7182818

print("---")

c2 = C2()
print(f"{c2.d=}")

c2.d = 3.1415927
print(f"{c2.d=}")
