import unittest
import src.pyvalidations as PyValidation


class TestInsideDe(unittest.TestCase):

    def test_pyvalidation_in_passed(self):
        data = {
            "north_america": "usa",
            "europe": "italy",
            "grade": "a",
        }
        rules = {
            "north_america": ["required", "in:usa,canada"],
            "europe": ["required", "not_in:china,japan"],
            "grade": ["required", "in:a,b"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_in_failed(self):
        data = {
            "north_america": "italy",
            "europe": "china",
            "grade": "u",
        }
        rules = {
            "north_america": ["required", "in:usa,canada"],
            "europe": ["required", "not_in:china,japan"],
            "grade": ["required", "in:a,b"],

        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'europe': ['Das ausgewählte europe ist ungültig.'],
                                               'grade': ['Das ausgewählte grade ist ungültig.'],
                                               'north_america': ['Das ausgewählte north_america ist ungültig.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
