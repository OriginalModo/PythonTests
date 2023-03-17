import pytest

from lesson.calculator import calculator, plus


def test_calc_plus():
    assert calculator('2+2') == 4


def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('not cool')
    assert 'Хотя бы 1 знак +-/*' == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as e:
        calculator('2+2+2')
    assert 'Ошибка: 2 целых числа' == e.value.args[0]


def test_plus():
    assert plus(2, 2) == 4


def test_plus_zeroes():
    assert plus(0, 0) == 0

def test_plus_zeroes_negative():
    assert plus(1, -1) == 0


if __name__ == '__main__':
    pytest.main()
