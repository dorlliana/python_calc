import unittest
from src.calc import calculator

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '+', '3']):
            self.assertEqual(calculator(), "Результат: 8.0")

    def test_subtraction(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '-', '3']):
            self.assertEqual(calculator(), "Результат: 2.0")

    def test_multiplication(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '*', '3']):
            self.assertEqual(calculator(), "Результат: 15.0")

    def test_division(self):
        with unittest.mock.patch('builtins.input', side_effect=['6', '/', '2']):
            self.assertEqual(calculator(), "Результат: 3.0")

    def test_division_by_zero(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '/', '0']):
            self.assertEqual(calculator(), "Помилка: Ділення на нуль!")

    def test_invalid_operator(self):
        with unittest.mock.patch('builtins.input', side_effect=['5', '%', '3']):
            self.assertEqual(calculator(), "Помилка: Невірна операція!")

    def test_invalid_input(self):
        with unittest.mock.patch('builtins.input', side_effect=['abc', '+', '3']):
            self.assertEqual(calculator(), "Помилка: Введіть числові значення!")

if __name__ == '__main__':
    unittest.main()
