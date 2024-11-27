import pytest
from main import factorials

def test_factorials_negative():
    with pytest.raises(ValueError, match="Input must be non-negative"):
        list(factorials(-5))

def test_factorials_zero():
    assert list(factorials(0)) == [1]

def test_factorials_positive():
    expected_values = [1, 2, 6, 24, 120]
    result = list(factorials(5))
    assert result == expected_values

def test_factorials_fractions():
    with pytest.raises(TypeError):
        list(factorials(2.5))

if __name__ == "__main__":
    pytest.main()
