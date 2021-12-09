import unittest
import src as PyValidation


class TestNullable(unittest.TestCase):

    def test_pyvalidation_nullable_passed(self):
        data = {
            "name_1": "",
            "name_2": "John",
            "name_3": None,
        }
        rules = {
            "name_1": ["nullable", "alpha"],
            "name_2": ["nullable", "alpha"],
            "name_3": ["nullable", "alpha"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_nullable_failed(self):
        data = {
            "name_1": "john 1",
            "number_2": "a2",
        }
        rules = {
            "name_1": ["nullable", "alpha"],
            "number_2": ["nullable", "numeric"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'name_1': ['The name_1 may only contain letters.'],
                                        'number_2': ['The number_2 must be a number.']}
                                    })


if __name__ == '__main__':
    unittest.main()
