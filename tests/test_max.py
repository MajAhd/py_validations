import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestMax(unittest.TestCase):

    def test_max(self):
        passed_1 = Rule.Max(10).is_maximum("20")
        passed_2 = Rule.Max("John").is_maximum("4")
        passed_3 = Rule.Max(21.1).is_maximum("22.1")
        failed_1 = Rule.Max(10).is_maximum("9")
        failed_2 = Rule.Max("john").is_maximum("3")
        failed_3 = Rule.Max(21.1).is_maximum("20.1")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

    def test_pyvalidation_max_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "max:40"],

        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_max_failed(self):
        data = {
            "age": 40,
        }
        rules = {
            "age": ["required", "max:30"],

        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'age': ['The age may not be greater than 30.']}
                                    })


if __name__ == '__main__':
    unittest.main()
