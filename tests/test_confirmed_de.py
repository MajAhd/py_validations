import unittest
import src.pyvalidations as PyValidation


class TestConfirmedDe(unittest.TestCase):

    def test_pyvalidation_confirmed(self):
        data_passed = {
            "password": "123456",
            "password_confirmation": "123456",
        }
        rules_1 = {
            "password": ["required", "confirmed"],
        }
        data_failed = {
            "password": "123456",
            "password_confirmed": "123456",
        }
        rules_2 = {
            "password": ["required", "confirmed"],
        }
        validate_passed = PyValidation.make(data_passed, rules_1, "de")
        self.assertEqual(validate_passed, {'errors': {}, 'failed': False})
        validate_failed = PyValidation.make(data_failed, rules_2 , "de")
        self.assertEqual(validate_failed,
                         {'errors': {'password': ['Die password-Bestätigung stimmt nicht überein.']},
                          'failed': True})


if __name__ == '__main__':
    unittest.main()
