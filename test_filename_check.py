import unittest

from dd1750Creator import contains_invalid_chars ,is_valid_filename

class Test_filename(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
