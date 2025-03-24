class Descriptor:
    def __get__(self, inst, owner=None):
        print(f"{inst=} {owner=}")
        ...
    def __set__(self, inst, val):
        ...
    def __delete__(self, inst):
        ...

class S:
    x = Descriptor()

obj = S()

print(obj.x)
print(S.x)

obj.x = 42
del obj.x

# -------------------------------------------

class Property:
    def __init__(self, func):
        self.fget = func

    def __get__(self, inst, owner=None):
        if inst is None:
            return self
        return self.fget(inst)

class A:
    def __init__(self, val):
        self._val = val

    @Property
    def val(self):
        return self._val

# -------------------------------------------

class ClassMethod:
    def __init__(self, func):
        self.func = func
    def __get__(self, inst, owner=None):
        if owner is None:
            owner = type(inst)
        return self.func.__get__(owner, owner)

class StaticMethod:
    def __init__(self, func):
        self.func = func
    def __get__(self, inst, owner=None):
        return self.func

class A:
    @ClassMethod
    def create(cls):
        return cls()

    @StaticMethod
    def something_static():
        print("something_static")

A.create()
A.something_static()

a=A()
a.create()
a.something_static()

# -------------------------------------------

class Vector3D:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

v3 = Vector3D(0.0, 0.0, 0.0)
v3.x = 1.0  # ok
# v.w = 1.0  # AttributeError
m = Vector3D.__dict__["x"]
m  # <member 'x' of 'Vector3D' objects>
keys = {"__get__", "__set__", "__delete__"}
set(dir(m)) & keys # {'__get__', '__delete__', '__set__'}

# -------------------------------------------

class A:
    pass

type(A.__dict__) # <class 'mappingproxy'>
obj = A.__dict__["__dict__"]
obj # <attribute '__dict__' of 'A' objects>
keys = {"__get__", "__set__", "__delete__"}
set(dir(obj)) & keys # {'__get__', '__delete__', '__set__'}

# -------------------------------------------

class GreaterThanValidator:
    def __init__(self, val):
        self.val = val
    def __set_name__(self, owner, name):
        self.name = name
    def __get__(self, inst, owner=None):
        if inst is None:
            return self
        return getattr(inst, f"_{self.name}")
    def __set__(self, inst, value):
        if not value > self.val:
            raise ValueError(f"value for {self.name} must be greater than {self.val}")
        setattr(inst, f"_{self.name}", value)

import dataclasses

@dataclasses.dataclass
class Item:
    name: str
    price: float = GreaterThanValidator(0.0)
    quantity: int = GreaterThanValidator(0)

banana = Item("Banana", 1.50, 15)
# banana = Item("Banana", 1.50, 0)  # ValueError
# banana = Item("Banana", -1.50, 15)  # ValueError
