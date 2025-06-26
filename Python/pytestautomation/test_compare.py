import pytest
@pytest.mark.great
def test_compare():
    num=100
    assert num>100

@pytest.mark.great    
def test_greaterequal():
    num=100
    assert num>=100

@pytest.mark.less    
def test_less():
    num=100
    assert num<200