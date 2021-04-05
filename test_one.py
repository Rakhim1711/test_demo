import pytest

@pytest.mark.one
def unit_one(x):
    return x + 20

@pytest.mark.one
def test_unit():
    assert unit_one(20) == 40
