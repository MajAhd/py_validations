import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestMin(unittest.TestCase):

    def test_min(self):
        passed_1 = Rule.Min(11).is_minimum("10")
        failed_1 = Rule.Min(9).is_minimum("10")
        self.assertTrue(passed_1)
        self.assertFalse(failed_1)

    def test_pyvalidation_min_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {})

    def test_pyvalidation_min_failed(self):
        data = {
            "age": 17,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'age': ['The age must be at least 18.']})


if __name__ == '__main__':
    unittest.main()
