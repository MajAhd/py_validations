import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestInside(unittest.TestCase):

    def test_is_in(self):
        passed_1 = Rule.Inside(5).is_in("1,2,3,4,5")
        passed_2 = Rule.Inside("5").is_in("1,2,3,4,5")
        passed_3 = Rule.Inside("Iran").is_in("Iran,USA,UK")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        failed_1 = Rule.Inside(5).is_in("1,2,3,4")
        failed_2 = Rule.Inside("5").is_in("1,2,3,4")
        failed_3 = Rule.Inside("iran").is_in("Iran,USA,UK")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

    def test_is_not_in(self):
        passed_1 = Rule.Inside(5).is_not_in("1,2,3,4")
        passed_2 = Rule.Inside("5").is_not_in("1,2,3,4")
        passed_3 = Rule.Inside("UK").is_not_in("Iran,USA")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        failed_1 = Rule.Inside(5).is_not_in("1,2,3,4,5")
        failed_2 = Rule.Inside("5").is_not_in("1,2,3,4,5")
        failed_3 = Rule.Inside("Iran").is_not_in("Iran,USA,UK")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

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
        validate = PyValidation.PyValidation(data, rules).make()
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
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'europe': ['The selected europe is invalid.'],
                                        'grade': ['The selected grade is invalid.'],
                                        'north_america': ['The selected north_america is invalid.']}
                                    })


if __name__ == '__main__':
    unittest.main()
