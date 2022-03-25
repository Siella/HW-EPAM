import pytest

from homework11.hw1 import (ColorsEnum, InvalidClassDef, SimplifiedEnum,
                            SizesEnum)


def test_simplified_enum():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"

    with pytest.raises(AttributeError) as excinfo:
        ColorsEnum.PINK == "PINK"
    assert "has no attribute 'PINK'" in str(excinfo.value)

    with pytest.raises(InvalidClassDef) as excinfo:
        class BadEnum(metaclass=SimplifiedEnum):
            pass
    assert 'not "__keys" attribute!' in str(excinfo.value)
