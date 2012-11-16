import csvquerytool
import unittest

class GuessTypeTests(unittest.TestCase):

    def _test_type(self, sample_data, sql_type, python_type):
        cast_func, guessed_type = csvquerytool.guess_type(sample_data)
        self.assertEqual(guessed_type, sql_type)
        for ele in sample_data:
            self.assertIsInstance(cast_func(ele), python_type)

    def test_float_type(self):
        sample_data = ['1.532', '-512.321', '0.4']
        self._test_type(sample_data, 'FLOAT', float)

    def test_integer_type(self):
        sample_data = ['-53', '3123', '0']
        self._test_type(sample_data, 'INTEGER', int)

    def test_text_type(self):
        sample_data = ['hello', 'world']
        self._test_type(sample_data, 'TEXT', unicode)

    def test_blob_type(self):
        sample_data = [chr(195) + chr(40)] # invalid utf-8 string
        self._test_type(sample_data, 'BLOB', bytes)

if __name__ == "__main__":
    unittest.main()
