import unittest
import src.pyvalidations as PyValidation


class TestDifferentDe(unittest.TestCase):

    def test_pyvalidation_different_passed(self):
        data = {
            "num_diff": 234,
            "str_diff": "MQ234",
            "num_eq": 100,
            "str_eq": "MQ100",
            "num_gt": 101,
            "num_gte": 200,
            "str_gt": "MAQ200",
            "str_gte": "MQ200",
            "num_lt": 99,
            "num_lte": 199,
            "str_lt": "abc",
            "str_lte": "abcd",
        }
        rules = {
            "num_diff": ["required", "different:233"],
            "str_diff": ["required", "different:MQ233"],
            "num_eq": ["required", "equal:100"],
            "str_eq": ["required", "equal:MQ100"],
            "num_gt": ["required", "gt:100"],
            "num_gte": ["required", "gte:200"],
            "str_gt": ["required", "gt:MQ200"],
            "str_gte": ["required", "gte:MQ200"],
            "num_lt": ["required", "lt:100"],
            "num_lte": ["required", "lte:200"],
            "str_lt": ["required", "lt:ABCD"],
            "str_lte": ["required", "lte:ABCD"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_different_failed(self):
        data = {
            "num_diff": 233,
            "str_diff": "MQ233",
            "num_eq": 200,
            "str_eq": "MQ200",
            "num_gt": 100,
            "num_gte": 199,
            "str_gt": "MQ200",
            "str_gte": "MQ20",
            "num_lt": 100,
            "num_lte": 201,
            "str_lt": "abcdef",
            "str_lte": "abcde",
        }
        rules = {
            "num_diff": ["required", "different:233"],
            "str_diff": ["required", "different:MQ233"],
            "num_eq": ["required", "equal:100"],
            "str_eq": ["required", "equal:MQ100"],
            "num_gt": ["required", "gt:100"],
            "num_gte": ["required", "gte:200"],
            "str_gt": ["required", "gt:MQ200"],
            "str_gte": ["required", "gte:MQ200"],
            "num_lt": ["required", "lt:100"],
            "num_lte": ["required", "lte:200"],
            "str_lt": ["required", "lt:ABCD"],
            "str_lte": ["required", "lte:ABCD"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'num_diff': ['Das num_diff muss sich von 233 unterscheiden.'],
                                               'num_eq': ['Das num_eq muss gleich 100 sein.'],
                                               'num_gt': ['Das num_gt muss größer als 100 sein.'],
                                               'num_gte': ['Das num_gte muss größer oder gleich 200 sein.'],
                                               'num_lt': ['Das num_lt muss kleiner als 100 sein.'],
                                               'num_lte': ['Das num_lte muss kleiner oder gleich 200 sein.'],
                                               'str_diff': ['Das str_diff muss sich von MQ233 unterscheiden.'],
                                               'str_eq': ['Das str_eq muss gleich MQ100 sein.'],
                                               'str_gt': ['Das str_gt muss größer als MQ200 sein.'],
                                               'str_gte': ['Das str_gte muss größer oder gleich MQ200 sein.'],
                                               'str_lt': ['Das str_lt muss kleiner als ABCD sein.'],
                                               'str_lte': ['Das str_lte muss kleiner oder gleich ABCD sein.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
