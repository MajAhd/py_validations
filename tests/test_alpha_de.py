import unittest
import src.pyvalidations as PyValidation


class TestAlphaDe(unittest.TestCase):

    def test_pyvalidation_alpha_failed(self):
        data = {
            "name": "John Doe 2021",
            "user_name": 920,
            "start_code": "G223other_string",
            "end_code": "other_stringG222"
        }
        rules = {
            "name": ["required", "alpha"],
            "user_name": ["required", "string"],
            "start_code": ["required", "start_with:G123"],
            "end_code": ["required", "end_with:G123"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'end_code': ['Das end_code darf nur mit G123 enden.'],
                                               'name': ['Das name darf nur Buchstaben enthalten.'],
                                               'start_code': ['Das start_code darf nur mit G123 beginnen.'],
                                               'user_name': ['Das user_name darf nur Strings enthalten.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
