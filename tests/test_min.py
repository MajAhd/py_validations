import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestMin(unittest.TestCase):

    def test_min(self):
        passed_1 = Rule.Min(11).is_minimum("10")
        passed_2 = Rule.Min("john").is_minimum("4")
        passed_3 = Rule.Min(21.1).is_minimum("21.1")
        failed_1 = Rule.Min(9).is_minimum("10")
        failed_2 = Rule.Min("john").is_minimum("5")
        failed_3 = Rule.Min(21.1).is_minimum("22.1")
        self.assertTrue(passed_1)
        self.assertFalse(failed_1)
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

    def test_pyvalidation_min_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_min_failed(self):
        data = {
            "age": 17,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'age': ['The age must be at least 18.']}
                                    })


if __name__ == '__main__':
    unittest.main()
