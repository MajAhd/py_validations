import unittest

import src.pyvalidations as PyValidation


class TestMaxDe(unittest.TestCase):

    def test_pyvalidation_max_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "max:40"],

        }
        validate = PyValidation.make(data, rules , "de")
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_max_failed(self):
        data = {
            "age": 40,
        }
        rules = {
            "age": ["required", "max:30"],

        }
        validate = PyValidation.make(data, rules , "de")
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'age': ['Das age darf nicht größer als 30 sein.']}
                                    })


if __name__ == '__main__':
    unittest.main()
