import unittest
import src.pyvalidations as PyValidation


class TestNumberDe(unittest.TestCase):

    def test_pyvalidation_number_passed(self):
        data = {
            "month": 30,
            "year": 2020,
        }
        rules = {
            "month": ["required", "numeric"],
            "year": ["required", "digits:4"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_number_failed(self):
        data = {
            "month": "a30",
            "year": 202,
        }
        rules = {
            "month": ["required", "numeric"],
            "year": ["required", "digits:4"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'month': ['Das month muss eine Zahl sein.'],
                                               'year': ['Das year muss aus 4 Ziffern bestehen.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
