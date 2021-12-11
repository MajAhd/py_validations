import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestBoolean(unittest.TestCase):

    def test_accepted(self):
        passed_1 = Rule.Boolean(True).is_boolean()
        passed_2 = Rule.Boolean(False).is_boolean()
        passed_3 = Rule.Boolean(0).is_boolean()
        passed_4 = Rule.Boolean(1).is_boolean()
        failed_1 = Rule.Boolean("0").is_boolean()
        failed_2 = Rule.Boolean("1").is_boolean()
        failed_3 = Rule.Boolean("true").is_boolean()
        failed_4 = Rule.Boolean("false").is_boolean()
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)

    def test_pyvalidation_boolean(self):
        data = {
            "bool_1": True,
            "bool_2": False,
            "bool_3": 0,
            "bool_4": 1,
            "bool_5": "1",
            "bool_6": "0",
            "bool_7": "false",
            "bool_8": "true",

        }
        rules = {
            "bool_1": ["required", "boolean"],
            "bool_2": ["required", "boolean"],
            "bool_3": ["required", "boolean"],
            "bool_4": ["required", "boolean"],
            "bool_5": ["required", "boolean"],
            "bool_6": ["required", "boolean"],
            "bool_7": ["required", "boolean"],
            "bool_8": ["required", "boolean"],
        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'errors': {'bool_5': ['The bool_5 may only boolean value : true , false , 1 '
                                  'or 0.'],
                       'bool_6': ['The bool_6 may only boolean value : true , false , 1 '
                                  'or 0.'],
                       'bool_7': ['The bool_7 may only boolean value : true , false , 1 '
                                  'or 0.'],
                       'bool_8': ['The bool_8 may only boolean value : true , false , 1 '
                                  'or 0.']},
            'failed': True})


if __name__ == '__main__':
    unittest.main()
