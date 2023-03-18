from asyncio.windows_events import NULL
import unittest
import pandas as pd  

from dd1750Creator import (contains_invalid_chars, is_valid_filename, get_items_to_print_to_1750, get_inventory, combine_same_items, format_for_1750, char_limit_items, number_of_items, fill_box_field)

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

        data={'LIN #': ['09065N','09065N','09065N','80506N'], 'COMMON NAME' : ['Garmin GPS 401', 'Garmin GPS 401', 'Garmin GPS 601', 'MULTI CAM RUCK'], 'SERIAL' : ['1LR061007','1LR061161','58A022747', 'A0'], 'PRINT DD-1750' : ['x','x','x','x']}
        expected_result = pd.DataFrame(data)

        self.assertEqual(str(items.to_numpy()),str(expected_result.to_numpy()))

    '''also tests get_inventory() and get_items_to_print_to_1750()
    must use simple sheet test.xlsx
    '''
    def test_combine_same_items(self):
        inventory = get_inventory()
        items = get_items_to_print_to_1750(inventory)
        items_to_print = combine_same_items(items)

        data={'COMMON NAME' : ['Garmin GPS 401', 'Garmin GPS 601', 'MULTI CAM RUCK'], 'SERIAL' : ['1LR061007, 1LR061161','58A022747', 'A0']}
        expected_result = pd.DataFrame(data)
        self.assertEqual(str(items_to_print), str(expected_result))
    
    def test_format_for_1750(self):
        inventory = get_inventory()
        items = get_items_to_print_to_1750(inventory)
        items_to_print = combine_same_items(items)
        list_1750 = format_for_1750(items_to_print)
        expected_output = ['Garmin GPS 401 S/n: 1LR061007, 1LR061161', 'Garmin GPS 601 S/n: 58A022747', 'MULTI CAM RUCK S/n: A0']
        self.assertEqual(list_1750, expected_output)

    def test_char_limit_items(self):
        s = 'Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161'
        s2 = 'Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161,3 ,4522 , 232, 1LR061007, 1LR061007, 1LR061007, 1LR061007, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161'
        test_data = [s, 'Smae 343344535', 'ff', s2, 'lass s/n: 4']

        expected_result = ['Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007, 1LR061161, 1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161','Smae 343344535', 'ff', 'Garmin GPS 401 S/n: 1LR061007, 1LR061007, 1LR061007, 1LR061007, 1LR061161, 1LR061161, 1LR061161,', '1LR061161, 1LR061161, 1LR061161,3 ,4522 , 232, 1LR061007, 1LR061007, 1LR061007, 1LR061007,', '1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161, 1LR061161', 'lass s/n: 4']

        result = char_limit_items(test_data)
        self.assertEqual(result, expected_result)
    
    def test_number_of_items(self):
        data = ['Garmin GPS 401 S/n: 1LR061007, 1LR061161', 'Garmin GPS 601 S/n: 58A022747, 1LR061007, 1LR061161', 'MULTI CAM RUCK S/n: A0']
        res = number_of_items(data[0])
        self.assertEqual(res, 2)
        res = number_of_items(data[1])
        self.assertEqual(res, 3)
        res = number_of_items(data[2])
        self.assertEqual(res, 1)
        res = number_of_items('no serials')
        self.assertEqual(res, 1)

    def test_fill_box_field(self):
        fillable_fields_dict = {'box_1': '', 'contents_1': '', 'unit_1': '', 'init_1': '', 'box_2': '', 'contents_2': '', 'unit_2': '', 'init_2': '', 'spares_2': '', 'box_3': '', 'contents_3': '', 'unit_3': '', 'init_3': '', 'spares_3': '', 'box_4': '', 'contents_4': '', 'unit_4': '', 'init_4': '', 'spares_4': '', 'box_5': '', 'contents_5': '', 'unit_5': '', 'init_5': '', 'spares_5': '', 'contents_6': '', 'unit_6': '', 'init_6': '', 'spares_6': '', 'box_6': '', 'init_7': '', 'spares_7': '', 'box_7': '', 'contents_7': '', 'unit_7': '', 'box_8': '', 'contents_8': '', 'unit_8': '', 'init_8': '', 'spares_8': '', 'box_9': '', 'contents_9': '', 'unit_9': '', 'init_9': '', 'spares_9': '', 'box_10': '', 'contents_10': '', 'unit_10': '', 'init_10': '', 'spares_10': '', 'box_11': '', 'contents_11': '', 'unit_11': '', 'init_11': '', 'spares_11': '', 'box_12': '', 'contents_12': '', 'unit_12': '', 'init_12': '', 'spares_12': '', 'box_13': '', 'contents_13': '', 'unit_13': '', 'init_13': '', 'spares_13': '', 'box_14': '', 'contents_14': '', 'unit_14': '', 'init_14': '', 'spares_14': '', 'box_15': '', 'contents_15': '', 'unit_15': '', 'init_15': '', 'spares_15': '', 'box_16': '', 'contents_16': '', 'unit_16': '', 'init_16': '', 'spares_16': '', 'box_17': '', 'contents_17': '', 'unit_17': '', 'init_17': '', 'spares_17': '', 'box_18': '', 'contents_18': '', 'unit_18': '', 'init_18': '', 'spares_18': '', 'certname': '', 'end_item': '', 'packed_by': '', 'no_boxes': '', 'req_no': '', 'order_no': '', 'date': '', 'total_pages': '', 'spares_1': '', 'cur_page': '', 'total_1': '', 'total_2': '', 'total_3': '', 'total_6': '', 'total_4': '', 'total_5': '', 'total_7': '', 'total_8': '', 'total_9': '', 'total_10': '', 'total_11': '', 'total_12': '', 'total_13': '', 'total_14': '', 'total_15': '', 'total_16': '', 'total_17': '', 'total_18': ''}
        expected_dict = {'box_1': '', 'contents_1': '', 'unit_1': '', 'init_1': '', 'box_2': '', 'contents_2': '', 'unit_2': '', 'init_2': '', 'spares_2': '', 'box_3': '', 'contents_3': '', 'unit_3': '', 'init_3': '', 'spares_3': '', 'box_4': '', 'contents_4': '', 'unit_4': '', 'init_4': '', 'spares_4': '', 'box_5': '', 'contents_5': '', 'unit_5': '', 'init_5': '', 'spares_5': '', 'contents_6': '', 'unit_6': '', 'init_6': '', 'spares_6': '', 'box_6': '', 'init_7': '', 'spares_7': '', 'box_7': '', 'contents_7': '', 'unit_7': '', 'box_8': '', 'contents_8': '', 'unit_8': '', 'init_8': '', 'spares_8': '', 'box_9': '', 'contents_9': '', 'unit_9': '', 'init_9': '', 'spares_9': '', 'box_10': '', 'contents_10': '', 'unit_10': '', 'init_10': '', 'spares_10': '', 'box_11': '', 'contents_11': '', 'unit_11': '', 'init_11': '', 'spares_11': '', 'box_12': '', 'contents_12': '', 'unit_12': '', 'init_12': '', 'spares_12': '', 'box_13': '', 'contents_13': '', 'unit_13': '', 'init_13': '', 'spares_13': '', 'box_14': '', 'contents_14': '', 'unit_14': '', 'init_14': '', 'spares_14': '', 'box_15': '', 'contents_15': '', 'unit_15': '', 'init_15': '', 'spares_15': '', 'box_16': '', 'contents_16': '', 'unit_16': '', 'init_16': '', 'spares_16': '', 'box_17': '', 'contents_17': '', 'unit_17': '', 'init_17': '', 'spares_17': '', 'box_18': '', 'contents_18': '', 'unit_18': '', 'init_18': '', 'spares_18': '', 'certname': '', 'end_item': '', 'packed_by': '', 'no_boxes': '', 'req_no': '', 'order_no': '', 'date': '', 'total_pages': '', 'spares_1': '', 'cur_page': '', 'total_1': '', 'total_2': '', 'total_3': '', 'total_6': '', 'total_4': '', 'total_5': '', 'total_7': '', 'total_8': '', 'total_9': '', 'total_10': '', 'total_11': '', 'total_12': '', 'total_13': '', 'total_14': '', 'total_15': '', 'total_16': '', 'total_17': '', 'total_18': ''}
        res_dict = fill_box_field(1, "GPS", fillable_fields_dict)
        expected_dict['box_1'] = "GPS"
        self.assertEqual(res_dict, expected_dict)

        res_dict = fill_box_field(3, "Ruck", fillable_fields_dict)
        expected_dict['box_3'] = "Ruck"
        self.assertEqual(res_dict, expected_dict)
        
        res_dict = fill_box_field(18, "M-110 S/n 2342342", fillable_fields_dict)
        expected_dict['box_18'] = "M-110 S/n 2342342"
        self.assertEqual(res_dict, expected_dict)

        res_dict = fill_box_field(19, "PC s/n 234324", fillable_fields_dict)
        self.assertEqual(res_dict, expected_dict)


         
if __name__ == '__main__':
    unittest.main()
