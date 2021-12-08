import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestMax(unittest.TestCase):

    def test_max(self):
        passed_1 = Rule.Max(10).is_maximum("20")
        failed_1 = Rule.Max(10).is_maximum("9")
        self.assertTrue(passed_1)
        self.assertFalse(failed_1)

    def test_pyvalidation_max_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "max:40"],

        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {})

    def test_pyvalidation_max_failed(self):
        data = {
            "age": 40,
        }
        rules = {
            "age": ["required", "max:30"],

        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'age': ['The age may not be greater than 30.']})


if __name__ == '__main__':
    unittest.main()
