import unittest
import pyvalidations.rules as Rule
import pyvalidations as PyValidation


class TestDateTime(unittest.TestCase):

    def test_is_date(self):
        is_date_passed = Rule.DateTime("1990-04-17").is_date()
        is_date_failed = Rule.DateTime("1990-13-17").is_date()
        self.assertTrue(is_date_passed)
        self.assertFalse(is_date_failed, "only 12 month accepted")

    def test_is_time(self):
        is_time_passed_1 = Rule.DateTime("11:00").is_time()
        is_time_passed_2 = Rule.DateTime("11:00am").is_time()
        is_time_passed_3 = Rule.DateTime("14:20").is_time()
        is_time_failed_1 = Rule.DateTime("12:60").is_time()
        self.assertTrue(is_time_passed_1)
        self.assertTrue(is_time_passed_2)
        self.assertTrue(is_time_passed_3)
        self.assertFalse(is_time_failed_1, "minute between 0 to 59")

    def test_is_datetime(self):
        is_datetime_passed_1 = Rule.DateTime("1990-04-17 11:00").is_date_time()
        is_datetime_failed_1 = Rule.DateTime("1990-13-17 11:60").is_date_time()
        self.assertTrue(is_datetime_passed_1)
        self.assertFalse(is_datetime_failed_1, "min 60 and month 13 mot correct")

    def test_is_timezone(self):
        is_timezone_passed_1 = Rule.DateTime("+04:30").is_timezone()
        is_timezone_passed_2 = Rule.DateTime("-01:00").is_timezone()
        is_timezone_failed_1 = Rule.DateTime("04:30").is_timezone()
        is_timezone_failed_2 = Rule.DateTime("0430").is_timezone()
        self.assertTrue(is_timezone_passed_1)
        self.assertTrue(is_timezone_passed_2)
        self.assertFalse(is_timezone_failed_1)
        self.assertFalse(is_timezone_failed_2)

    def test_is_date_equal(self):
        is_date_equal_passed = Rule.DateTime("1990-04-17").date_equals("1990-04-17")
        is_date_equal_failed = Rule.DateTime("1990-04-17").date_equals("1990-05-17")
        self.assertTrue(is_date_equal_passed)
        self.assertFalse(is_date_equal_failed)

    def test_is_date_after(self):
        is_date_after_passed = Rule.DateTime("1990-04-17").is_after("1990-04-16")
        is_date_after_failed = Rule.DateTime("1990-04-17").is_after("1990-04-17")
        self.assertTrue(is_date_after_passed)
        self.assertFalse(is_date_after_failed)

    def test_is_date_equal_after(self):
        is_date_ea_passed = Rule.DateTime("1990-04-17").is_after_or_equal("1990-04-16")
        is_date_ea_passed_2 = Rule.DateTime("1990-04-17").is_after_or_equal("1990-04-17")
        is_date_ea_failed = Rule.DateTime("1990-04-16").is_after_or_equal("1990-04-17")
        self.assertTrue(is_date_ea_passed)
        self.assertTrue(is_date_ea_passed_2)
        self.assertFalse(is_date_ea_failed)

    def test_is_date_before(self):
        is_date_before_passed = Rule.DateTime("1990-04-17").is_before("1990-04-18")
        is_date_before_failed = Rule.DateTime("1990-04-17").is_before("1990-04-17")
        self.assertTrue(is_date_before_passed)
        self.assertFalse(is_date_before_failed)

    def test_is_date_equal_before(self):
        is_date_ba_passed = Rule.DateTime("1990-04-17").is_before_or_equal("1990-04-18")
        is_date_ba_passed_2 = Rule.DateTime("1990-04-17").is_before_or_equal("1990-04-17")
        is_date_ba_failed = Rule.DateTime("1990-04-16").is_before_or_equal("1990-04-15")
        self.assertTrue(is_date_ba_passed)
        self.assertTrue(is_date_ba_passed_2)
        self.assertFalse(is_date_ba_failed)

    def test_pyvalidation_datetime_passed(self):
        data = {
            "birthdate": "1990-04-17",
            "start_time": "13:30",
            "expired": "2020-06-28 12:20",
            "my_zone": "+04:30",
        }
        rules = {
            "birthdate": ["required", "date"],
            "start_time": ["required", "time"],
            "expired": ["required", "datetime"],
            "my_zone": ["required", "timezone"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_datetime_failed(self):
        data = {
            "birthdate": "199004-17",
            "start_time": "1330",
            "expired": "2020-06-28-1220",
            "my_zone": "04:30",
        }
        rules = {
            "birthdate": ["required", "date"],
            "start_time": ["required", "time"],
            "expired": ["required", "datetime"],
            "my_zone": ["required", "timezone"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {'errors': {'birthdate': ['The birthdate is not a valid date.'],
                                               'expired': ['The expired is not a valid datetime.'],
                                               'my_zone': ['The my_zone is not a valid Timezone.'],
                                               'start_time': ['The start_time is not a valid time.']},
                                    'failed': True})

    def test_pyvalidation_datetime_different_passed(self):
        data = {
            "eq_bd": "1990-04-17",
            "after_bd": "1990-04-20",
            "after_equal_bd": "1990-04-18",
            "before_bd": "1990-04-16",
            "before_equal_bd": "1990-04-17",
        }
        rules = {
            "eq_bd": ["required", "date_equals:1990-04-17"],
            "after_bd": ["required", "after:1990-04-17"],
            "after_equal_bd": ["required", "after_or_equal:1990-04-17"],
            "before_bd": ["required", "before:1990-04-17"],
            "before_equal_bd": ["required", "before_or_equal:1990-04-17"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_datetime_different_failed(self):
        data = {
            "eq_bd": "1990-04-14",
            "after_bd": "1990-04-16",
            "after_equal_bd": "1990-04-15",
            "before_bd": "1990-04-17",
            "before_equal_bd": "1990-04-18",
        }
        rules = {
            "eq_bd": ["required", "date_equals:1990-04-17"],
            "after_bd": ["required", "after:1990-04-17"],
            "after_equal_bd": ["required", "after_or_equal:1990-04-17"],
            "before_bd": ["required", "before:1990-04-17"],
            "before_equal_bd": ["required", "before_or_equal:1990-04-17"],
        }
        validate = PyValidation.PyValidations(data, rules).make()
        self.assertEqual(validate, {'errors': {'after_bd': ['The after_bd must be a date after to 1990-04-17.'],
                                               'after_equal_bd': ['The after_equal_bd must be a date after or '
                                                                  'equal to 1990-04-17.'],
                                               'before_bd': ['The before_bd must be a date before to 1990-04-17.'],
                                               'before_equal_bd': ['The before_equal_bd must be a date before or '
                                                                   'equal to 1990-04-17.'],
                                               'eq_bd': ['The eq_bd must be a date equal to 1990-04-17.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
