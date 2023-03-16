import unittest

from dd1750_creator import contains_invalid_chars

class Test_filename(unittest.TestCase):
    def new_method(self):
        self.assertEqual(contains_invalid_chars("goodfile.@@"), False)
       

if __name__ == '__main__':
    unittest.main()
