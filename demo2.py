class D:
    def __init__(self):
        print('D __init__')

    def __get__(self, inst, owner=None):
        print('__get__')
        return getattr(inst, "_val", 42.0)

    def __set__(self, inst, val):
        print(f"__set__ {val=}")
        inst._val = val

    def __delete__(self, inst):
        print('__delete__')
        del inst._val

class C2():
    d = D()

    def __init__(self):
        self.__dict__['d'] = 2.7182818

c2 = C2()
print(f"{c2.d=}")

c2.d = 3.1415927
print(f"{c2.d=}")
