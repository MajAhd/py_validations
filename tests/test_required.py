import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestRequired(unittest.TestCase):

    def test_is_required(self):
        passed = Rule.Required("My Value").is_required()
        not_passed = Rule.Required("").is_required()
        null_value = Rule.Required(None).is_required()
        self.assertTrue(passed, "Required has value:  True")
        self.assertFalse(not_passed, "Required is empty : False")
        self.assertFalse(null_value, "Required is Null : False")

    def test_pyvalidation_is_required(self):
        data = {
            "name_1": "Majid",
            "name_2": "",
            "name_3": None,
        }
        rules = {
            "name": ["required"],
            "name_2": ["required"],
            "name_3": ["required"],
        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'failed': True,
                                    "errors": {
                                        'name_2': ['The name_2 field is required.'],
                                        'name_3': ['The name_3 field is required.']}
                                    })


if __name__ == '__main__':
    unittest.main()
