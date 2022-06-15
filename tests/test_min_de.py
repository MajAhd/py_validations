import unittest
import src.pyvalidations as PyValidation


class TestMinDe(unittest.TestCase):

    def test_pyvalidation_min_passed(self):
        data = {
            "age": 20,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.make(data, rules , "de")
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_min_failed(self):
        data = {
            "age": 17,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.make(data, rules , "de")
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'age': ['Das age muss mindestens 18 sein.']}
                                    })


if __name__ == '__main__':
    unittest.main()
