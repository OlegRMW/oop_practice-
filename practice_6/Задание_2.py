import unittest


def days_in_month(month, leap=False):

    if not isinstance(month, int) or month < 1 or month > 12:
        raise ValueError("Номер месяца должен быть целым числом от 1 до 12")
    
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    elif month in [4, 6, 9, 11]:
        return 30
    
    elif month == 2:
        return 29 if leap else 28
    else:
        raise ValueError("Некорректный номер месяца")


class TestDaysInMonth(unittest.TestCase):
    
    def test_31_days_months(self):
        months_31 = [1, 3, 5, 7, 8, 10, 12]
        for month in months_31:
            with self.subTest(month=month):
                self.assertEqual(days_in_month(month), 31)
                self.assertEqual(days_in_month(month, leap=True), 31)
                self.assertEqual(days_in_month(month, leap=False), 31)
    
    def test_30_days_months(self):
        months_30 = [4, 6, 9, 11]
        for month in months_30:
            with self.subTest(month=month):
                self.assertEqual(days_in_month(month), 30)
                self.assertEqual(days_in_month(month, leap=True), 30)
                self.assertEqual(days_in_month(month, leap=False), 30)
    
    def test_february_non_leap(self):
        """Тест февраля в невисокосный год"""
        self.assertEqual(days_in_month(2), 28)
        self.assertEqual(days_in_month(2, leap=False), 28)
    
    def test_february_leap(self):
        """Тест февраля в високосный год"""
        self.assertEqual(days_in_month(2, leap=True), 29)
    
    def test_invalid_month_low(self):
        """Тест некорректного номера месяца (меньше 1)"""
        with self.assertRaises(ValueError):
            days_in_month(0)
        with self.assertRaises(ValueError):
            days_in_month(-1)
    
    def test_invalid_month_high(self):
        """Тест некорректного номера месяца (больше 12)"""
        with self.assertRaises(ValueError):
            days_in_month(13)
        with self.assertRaises(ValueError):
            days_in_month(100)
    
    def test_invalid_month_type(self):
        """Тест некорректного типа месяца"""
        with self.assertRaises(ValueError):
            days_in_month("1")
        with self.assertRaises(ValueError):
            days_in_month(1.5)
        with self.assertRaises(ValueError):
            days_in_month(None)
    
    def test_all_months_non_leap(self):
        """Тест всех месяцев в невисокосный год"""
        expected = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month, expected_days in enumerate(expected, 1):
            with self.subTest(month=month):
                self.assertEqual(days_in_month(month, leap=False), expected_days)
    
    def test_all_months_leap(self):
        """Тест всех месяцев в високосный год"""
        expected = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month, expected_days in enumerate(expected, 1):
            with self.subTest(month=month):
                self.assertEqual(days_in_month(month, leap=True), expected_days)

if __name__ == '__main__':
    unittest.main()