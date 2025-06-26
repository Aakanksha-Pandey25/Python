import pytest
@pytest.fixture

def input_values():
    input=39
    return input

def test_divisible_by_3(input_values):
    assert input_values%3==0

def tes_divisible_by_6(input_values):
    assert input_values % 6 == 0