import unittest
from finance.salary import calculate_monthly_salary, annual_salary_from_monthly

class TestSalaryModule(unittest.TestCase):
    def test_calculate_monthly_salary(self):
        self.assertEqual(calculate_monthly_salary(120000), 10000)
        self.assertAlmostEqual(calculate_monthly_salary(75000), 6250)

    def test_annual_salary_from_monthly(self):
        self.assertEqual(annual_salary_from_monthly(10000), 120000)
        self.assertAlmostEqual(annual_salary_from_monthly(6250), 75000)

if __name__ == "__main__":
    unittest.main()
