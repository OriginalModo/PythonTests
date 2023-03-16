from unittest import TestCase, main
import doctest
from lesson import doctestt

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(doctestt))
    return tests



class TestDoctestt(TestCase):
    def test_zero_raises(self):
        with self.assertRaises(ValueError):
            doctestt.divide(10, 0)


if __name__ == "__main__":
    doctest.testmod()