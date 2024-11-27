import pytest
from main import factorials
@pytest.mark.parametrize("input_value, expected_output", [
    (0, [1]),  # factorials(0) should return [1]
    (1, [1]),  # factorials(1) should return [1]
    (3, [1, 2, 6]),  # factorials(3) should return [1, 2, 6]
])
def test_factorials_parametrize(input_value, expected_output):
    assert list(factorials(input_value)) == expected_output

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
