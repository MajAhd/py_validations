import unittest
import src.pyvalidations as PyValidation


class TestAcceptedDe(unittest.TestCase):

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
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'accept_6': ['Das accept_6 muss akzeptiert werden.'],
                                               'accept_7': ['Das accept_7 muss akzeptiert werden.'],
                                               'accept_8': ['Das accept_8 muss akzeptiert werden.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
