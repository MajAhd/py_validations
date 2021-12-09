import unittest
import pyvalidations.rules as Rule
import pyvalidations as PyValidation


class TestNumber(unittest.TestCase):

    def test_number(self):
        passed_1 = Rule.Number(210).is_numeric()
        passed_2 = Rule.Number("210").is_numeric()
        passed_3 = Rule.Number(2022).digits(4)
        passed_4 = Rule.Number("2022").digits(4)
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        failed_1 = Rule.Number("a220").is_numeric()
        failed_2 = Rule.Number(202).digits(4)
        failed_3 = Rule.Number(2020).digits("a4")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

    def test_pyvalidation_number_passed(self):
        data = {
            "month": 30,
            "year": 2020,
        }
        rules = {
            "month": ["required", "numeric"],
            "year": ["required", "digits:4"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
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
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {
            "failed": True,
            "errors": {
                'month': ['The month must be a number.'],
                'year': ['The year must be 4 digits.']}
        })


if __name__ == '__main__':
    unittest.main()
