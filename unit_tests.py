# We need to import unittest library and the class we are testing
import unittest
from ohjelma import Basket
import numbers


# We need to create a new testcase class by inheriting unittest.TestCase
class BasketTests(unittest.TestCase):

    # Setup method to create a test object
    def setUp(self):
        self.keijon_ostoskori = Basket("Keijo", ["kissa","pasi"], 20)

    # Teardown method to delete the test object
    def tearDown(self):
        del self.keijon_ostoskori

    # Let's test if variable customer is a string
    def test_is_customer_string(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.customer, str), "variable name should be string")

    # Let's test if variable price is a number
    def test_is_price_number(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.price, numbers.Number), "variable price should be a number")

    # Let's test if variable contents is a list
    def test_is_contents_list(self):
        self.assertTrue(isinstance(self.keijon_ostoskori.contents, list), "variable contents should be a list")

    # Let's test if add_product method works
    def test_adding_to_list(self):
        self.keijon_ostoskori.add_product("kala",1)
        self.assertIn("kala", self.keijon_ostoskori.contents, "add_product method did not add a product to list")

    # Let's test if delete_product method works
    def test_delete_from_list(self):
        self.keijon_ostoskori.delete_product("pasi",1)
        self.assertNotIn("pasi", self.keijon_ostoskori.contents, "delete_product method did not delete product from list")

    # Let's test does count_discount method work
    def test_count_discount(self):
        self.assertEqual(self.keijon_ostoskori.count_discount_price(10), 18, "count_discount_price does not count correct value")

    # Let's test does our count_discount raise TypeError with wrong type
    def test_count_discount_error_handling(self):
        self.assertRaises(TypeError, self.keijon_ostoskori.count_discount_price, "55")
            
            

if __name__ == '__main__':
    unittest.main()
