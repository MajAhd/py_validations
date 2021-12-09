import unittest
import src.rules as Rule
import src as PyValidation


class TestAccepted(unittest.TestCase):

    def test_accepted(self):
        passed_1 = Rule.Accepted("on").is_accepted()
        passed_2 = Rule.Accepted("yes").is_accepted()
        passed_3 = Rule.Accepted("true").is_accepted()
        passed_4 = Rule.Accepted(1).is_accepted()
        passed_5 = Rule.Accepted("1").is_accepted()
        failed_1 = Rule.Accepted("off").is_accepted()
        failed_2 = Rule.Accepted(0).is_accepted()
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        self.assertTrue(passed_5)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)

    def test_pyvalidation_accepted(self):
        data = {
            "accept_1": "on",
            "accept_2": "yes",
            "accept_3": "true",
            "accept_4": 1,
            "accept_5": "1",
            "accept_6": "off",
            "accept_7": "false",
            "accept_8": "0",

        }
        rules = {
            "accept_1": ["required", "accepted"],
            "accept_2": ["required", "accepted"],
            "accept_3": ["required", "accepted"],
            "accept_4": ["required", "accepted"],
            "accept_5": ["required", "accepted"],
            "accept_6": ["required", "accepted"],
            "accept_7": ["required", "accepted"],
            "accept_8": ["required", "accepted"],
        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'errors': {'accept_6': ['The accept_6 must be accepted.'],
                                               'accept_7': ['The accept_7 must be accepted.'],
                                               'accept_8': ['The accept_8 must be accepted.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
