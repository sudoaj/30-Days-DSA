# tests/test_tax.py
import unittest
from finance.tax import calculate_tax, net_income

class TestTaxModule(unittest.TestCase):
    def test_calculate_tax(self):
        self.assertEqual(calculate_tax(100000, 0.2), 20000)
        self.assertAlmostEqual(calculate_tax(75000, 0.18), 13500)

    def test_net_income(self):
        self.assertEqual(net_income(100000, 0.2), 80000)
        self.assertAlmostEqual(net_income(75000, 0.18), 61500)

if __name__ == "__main__":
    unittest.main()
