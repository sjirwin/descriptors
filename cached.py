class my_cached_property:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, inst, owner=None):
        if inst is None:
            return self
        ret = inst.__dict__[self.name] = self.func.__get__(inst, owner)() # self.func(inst)
        return ret

class A:
    @my_cached_property
    def v(self):
        print('computing v ...')
        return 42

print("---")

a = A()
print(f"{a.__dict__=}")
print(f"{a.v=}")

print("---")

print(f"{a.__dict__=}")
print(f"{a.v=}")
