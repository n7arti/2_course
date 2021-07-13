import unittest
from Project import Product

class ProductTestCase(unittest.TestCase):
    def Set(self):
        self.product_check = Product()

    def Check_name(self):
        self.assertEqual(self.product_check.name, "Apelsin")

    def Check_price(self):
        self.assertEqual(self.product_check.pricerub, 30)

    def Check_manfuc(self):
        self.assertEqual(self.product_check.manfac, "Ogorod")

if __name__ == "__main__":
    unittest.main()