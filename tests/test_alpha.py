import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestAlpha(unittest.TestCase):

    def test_alpha(self):
        passed_1 = Rule.Alpha("this + is - string 123").is_string()
        passed_2 = Rule.Alpha("this is string").is_alpha()
        passed_3 = Rule.Alpha("secretxcvvs").start_with("secret")
        passed_4 = Rule.Alpha("xcvszsecret").end_with("secret")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        failed_1 = Rule.Alpha(123).is_string()
        failed_2 = Rule.Alpha("is not alpha 123 + ").is_alpha()
        failed_3 = Rule.Alpha("showxcvvs").start_with("secret")
        failed_4 = Rule.Alpha("xcvszshow").end_with("secret")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)
        target_type = Rule.Alpha("secretxcvvs").start_with(111)
        self.assertFalse(target_type)

    def test_pyvalidation_alpha_passed(self):
        data = {
            "name": "John Doe",
            "user_name": "John_007",
            "start_code": "G123other_string",
            "end_code": "other_stringG123"
        }
        rules = {
            "name": ["required", "alpha"],
            "user_name": ["required", "string"],
            "start_code": ["required", "start_with:G123"],
            "end_code": ["required", "end_with:G123"],
        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {'errors': {}, 'failed': False})

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
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {'errors': {'end_code': ['The end_code may only end with G123.'],
                                               'name': ['The name may only contain letters.'],
                                               'start_code': [
                                                   'The start_code may only start with G123.'],
                                               'user_name': ['The user_name may only string.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
