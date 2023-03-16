from unittest import TestCase, main
from lesson.calculator import calculator


class Calculator(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    def test_minus(self):
        self.assertEqual(calculator('3-1'), 2)

    def test_multiple(self):
        self.assertEqual(calculator('4*4'), 16)

    def test_divine(self):
        self.assertEqual(calculator('4/2'), 2.0)

    def test_no_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('not cool')
        self.assertEqual('Хотя бы 1 знак +-/*', e.exception.args[0])

    def test_two_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+2+2')
        self.assertEqual('Ошибка: 2 целых числа', e.exception.args[0])

    def test_nany_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Ошибка: 2 целых числа', e.exception.args[0])


    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.2+3.0')
        self.assertEqual('Ошибка: 2 целых числа', e.exception.args[0])

    def test_string(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Ошибка: 2 целых числа', e.exception.args[0])




if __name__ == "__main__":
    main()



