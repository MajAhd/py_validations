import unittest
import src.pyvalidations.rules as Rule
import src as PyValidation


class TestConfirmed(unittest.TestCase):

    def test_confirmed(self):
        passed = Rule.Confirmation("123", "123").is_confirmed()
        failed = Rule.Confirmation("123", "abc").is_confirmed()

        self.assertTrue(passed)
        self.assertFalse(failed)

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

        validate_passed = PyValidation.PyValidations(data_passed, rules_1).make()
        self.assertEqual(validate_passed, {'errors': {}, 'failed': False})
        validate_failed = PyValidation.PyValidations(data_failed, rules_2).make()
        self.assertEqual(validate_failed, {'errors': {'password': ['The password confirmation does not match.']},
                                           'failed': True})


if __name__ == '__main__':
    unittest.main()
