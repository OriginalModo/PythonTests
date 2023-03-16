import pytest

from lesson.calculator import calculator


def test_plus():
    assert calculator('2+2') == 4

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('not cool')
    assert 'Хотя бы 1 знак +-/*' == error.value.args[0]


def test_two_signs():
    with pytest.raises(ValueError) as e:
        calculator('2+2+2')
    assert 'Ошибка: 2 целых числа' == e.value.args[0]

if __name__ == '__main__':
    pytest.main()
