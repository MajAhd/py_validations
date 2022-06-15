import unittest
import src.pyvalidations as PyValidation


class TestDateTimeDe(unittest.TestCase):

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
        validate = PyValidation.make(data, rules, "de")
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
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'birthdate': ['Das birthdate ist kein gültiges Datum.'],
                                               'expired': ['Das expired ist kein gültiges datetime.'],
                                               'my_zone': ['Das my_zone ist keine gültige Zeitzone.'],
                                               'start_time': ['Das start_time ist keine gültige Zeit.']},
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
        validate = PyValidation.make(data, rules, "de")
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
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'after_bd': ['Das after_bd muss ein Datum nach 1990-04-17 sein.'],
                                               'after_equal_bd': ['Das after_equal_bd muss ein Datum nach oder '
                                                                  'gleich 1990-04-17 sein.'],
                                               'before_bd': ['Das before_bd muss ein Datum vor 1990-04-17 sein.'],
                                               'before_equal_bd': ['Das before_equal_bd muss ein Datum vor oder '
                                                                   'gleich 1990-04-17 sein.'],
                                               'eq_bd': ['Das eq_bd muss ein Datum gleich 1990-04-17 sein.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
