import unittest
import src.rules as Rule
import src as PyValidation


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
            "accept_1": True,
            "accept_2": False,
            "accept_3": 0,
            "accept_4": 1,
            "accept_5": "1",
            "accept_6": "0",
            "accept_7": "false",
            "accept_8": "true",

        }
        rules = {
            "accept_1": ["required", "boolean"],
            "accept_2": ["required", "boolean"],
            "accept_3": ["required", "boolean"],
            "accept_4": ["required", "boolean"],
            "accept_5": ["required", "boolean"],
            "accept_6": ["required", "boolean"],
            "accept_7": ["required", "boolean"],
            "accept_8": ["required", "boolean"],
        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'errors': {'accept_5': ['The accept_5 may only boolean value : true , false , '
                                                            '1 or 0.'],
                                               'accept_6': ['The accept_6 may only boolean value : true , false , '
                                                            '1 or 0.'],
                                               'accept_7': ['The accept_7 may only boolean value : true , false , '
                                                            '1 or 0.'],
                                               'accept_8': ['The accept_8 may only boolean value : true , false , '
                                                            '1 or 0.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
