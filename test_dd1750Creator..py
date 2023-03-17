import unittest
import pandas as pd  

from dd1750Creator import contains_invalid_chars ,is_valid_filename, get_items_to_print_to_1750, get_inventory

class Test_dd1750Creator(unittest.TestCase):
    def test_contains_invalid_chars(self):
        self.assertFalse(contains_invalid_chars("goodfile.@@"))
        self.assertFalse(contains_invalid_chars("goood[]%%^^&&!@#``~~.,'{}"))
        self.assertTrue(contains_invalid_chars("bad<sdf"))
        self.assertTrue(contains_invalid_chars("bad>sdf"))
        self.assertTrue(contains_invalid_chars("b:adsdf"))
        self.assertTrue(contains_invalid_chars('bad"d'))
        self.assertTrue(contains_invalid_chars('bad"d'))
        self.assertTrue(contains_invalid_chars('bad/d'))
        self.assertTrue(contains_invalid_chars('b\\add'))
        self.assertTrue(contains_invalid_chars('bad|d'))
        self.assertTrue(contains_invalid_chars('bad?d'))
        self.assertTrue(contains_invalid_chars('bad*d'))

    def test_is_valid_filename(self):
        self.assertFalse(is_valid_filename())
    
    '''also tests get_inventory()
    '''
    def test_get_items_to_print_to_1750(self):
        inventory = get_inventory()
        items = get_items_to_print_to_1750(inventory)

        expected_result = pd.DataFrame({})

if __name__ == '__main__':
    unittest.main()
