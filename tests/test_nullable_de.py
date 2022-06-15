import unittest
import src.pyvalidations as PyValidation


class TestNullableDe(unittest.TestCase):

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
        validate = PyValidation.make(data, rules, "de")
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
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'name_1': ['Das name_1 darf nur Buchstaben enthalten.'],
                                               'number_2': ['Das number_2 muss eine Zahl sein.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
