class D:
    def __init__(self):
        print('D __init__')

    def __get__(self, inst, owner=None):
        print('__get__')
        return 3.1415927
    
class C1:
    d = D()

print(f"{C1().d=}")

class C2():
    d = D()

    def __init__(self):
        self.__dict__['d'] = 2.7182818

print(f"{C2().d=}")
