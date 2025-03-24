# Notes

## Attribute lookup - basic view

Given an atrribute named `attrib`, the lookup sequence is

1. data descriptors
1. `self.__dict__['attrib']`
1. non-data descriptors

## Hidden uses of descriptors

1. Class methods
1. Properties
1. Class methods and static methods
1. Slots
1. `__dict__`
1. Validators
1. SQLAlchemy Models

## Class methods are descriptors

```python
>>> class C:
...     def m(self):
...         print('m')
...
>>> C.m
<function C.m at 0x10334cd60>
>>> C.m.__get__
<method-wrapper '__get__' of function object at 0x10334cd60>
>>> C().m
<bound method C.m of <__main__.C object at 0x10333c980>>
>>> c = C()
>>> method = C.m.__get__(c, type(c))
>>> method
<bound method C.m of <__main__.C object at 0x1032a6c10>>
>>> method()
m
```

```python
class Function:
    # ... other function stuff

    def __get__(self, inst, owner=None):
        if owner is None:
            return self
        return ... # bound function thingy
```

## `__get__`, `__set__`, `__delete__` vs. `__getattr__`, `__setattr__`, `__delattr__`

- `__getattr__` are defined per class
- `__get__` are defined per attribute

## Descriptors and classes that define attribute access methods

- `__getattribute__(self, item)`: always called
  - `__getattr__(self, item)`: called if `__getattribute__` raises `AttributeError`
- `__setattr__(self, item, value)`: always called
- `__delattr__(self, item)`: always called

```python
class A:
    x = MyDescriptor()
    def __getattribute__(self, item):
        return object.__getattribute__(self, item)  # implements descriptor logic
    def __getattr__(self, item):
        ...
    def __setattr__(self, item, value):
        object.__setattr__(self, item, value)  # implements descriptor logic
    def __delattr__(self, item):
        object.__delattr__(self, item)  # implements descriptor logic
```

## Attribute lookup - full view

Given an atrribute named `attrib`, the lookup sequence is

1. data descriptors
1. `self.__dict__['attrib']`
1. non-data descriptors
1. class vars
1. raise AttributeError (which triggers `__getattr__`)
