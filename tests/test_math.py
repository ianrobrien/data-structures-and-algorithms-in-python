from algorithms.math import factorial, fibonacci


class TestMath:

    def test_factorial(self):
        assert (factorial(0) == 1)
        assert (factorial(1) == 1)
        assert (factorial(5) == 120)

    def test_fibonacci(self):
        assert (fibonacci(0) == 0)
        assert (fibonacci(1) == 1)
        assert (fibonacci(2) == 1)
        assert (fibonacci(5) == 5)
        assert (fibonacci(12) == 144)
