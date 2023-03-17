from asyncio.windows_events import NULL
import unittest
import pandas as pd  

from dd1750Creator import contains_invalid_chars ,is_valid_filename, get_items_to_print_to_1750, get_inventory, combine_same_items

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

        ''' this test is dependant on what the user enters
        '''
    def test_is_valid_filename(self):
        self.assertTrue(is_valid_filename())
    
    '''also tests get_inventory()
    must use simple sheet test.xlsx
    '''
    def test_get_items_to_print_to_1750(self):
        inventory = get_inventory()
        items = get_items_to_print_to_1750(inventory)

        data={'LIN #': ['09065N','09065N','09065N','09065N','80506N'], 'COMMON NAME' : ['Garmin GPS 401', 'Garmin GPS 401', 'Garmin GPS 601', 'Garmin GPS 601', 'MULTI CAM RUCK'], 'SERIAL' : ['1LR061007','1LR061161','58A022747','58A022766', 'A0'], 'PRINT DD-1750' : ['x','x','x','x','x']}
        expected_result = pd.DataFrame(data)
        #print('expected')
        #print(expected_result.info(verbose=True))
        #print('inventory')
        #print(inventory.info(verbose=True))
        self.assertEqual(str(items.to_numpy()),str(expected_result.to_numpy()), "Not equal")

    def test_combine_same_items(self):
        inventory = get_inventory()
        items = get_items_to_print_to_1750(inventory)
        items_to_print = combine_same_items(items)

        data={'LIN #': ['09065N','09065N','80506N'], 'COMMON NAME' : ['Garmin GPS 401', 'Garmin GPS 601', 'MULTI CAM RUCK'], 'SERIAL' : ['1LR061007, 1LR061161','58A022747, 58A022766', 'A0']}
        expected_result = pd.DataFrame(data)
        print('items to print')
        print(items_to_print)
        #self.assertEqual(str(items_to_print), str(expected_result))


if __name__ == '__main__':
    unittest.main()
