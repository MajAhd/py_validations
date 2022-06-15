import unittest
import src.pyvalidations as PyValidation


class TestBooleanDe(unittest.TestCase):

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
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'bool_5': ['Das bool_5 darf nur einen booleschen Wert haben: true '
                                                          ', false , 1 oder 0.'],
                                               'bool_6': ['Das bool_6 darf nur einen booleschen Wert haben: true '
                                                          ', false , 1 oder 0.'],
                                               'bool_7': ['Das bool_7 darf nur einen booleschen Wert haben: true '
                                                          ', false , 1 oder 0.'],
                                               'bool_8': ['Das bool_8 darf nur einen booleschen Wert haben: true '
                                                          ', false , 1 oder 0.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
