"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.

from enum import Enum


class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"


class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"


Should become:

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""


class InvalidClassDef(Exception):
    pass


class SimplifiedEnum(type):
    """
    Metaclass that creates a class instance with attributes
    given in __keys attribute.
    """
    def __new__(cls, *args, **kwargs):
        cls_instance = super().__new__(cls, *args, **kwargs)
        keys = ''.join(['_', cls_instance.__name__, '__keys'])
        try:
            for k in getattr(cls_instance, keys):
                if not hasattr(cls_instance, str(k)):
                    setattr(cls_instance, str(k), k)
        except AttributeError:
            raise InvalidClassDef('Class has not "__keys" attribute!')
        return cls_instance


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


if __name__ == '__main__':
    sizes = SizesEnum()
    colors = ColorsEnum()
    print(sizes.XS, colors.RED)
