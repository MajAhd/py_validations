import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestDifferent(unittest.TestCase):

    def test_different(self):
        passed_1 = Rule.Different("22").is_different(23)
        passed_2 = Rule.Different(33).is_different(34)
        passed_3 = Rule.Different("22.3").is_different(22.4)
        passed_4 = Rule.Different(22.3).is_different(22.4)
        passed_5 = Rule.Different("str").is_different("str_1")

        failed_1 = Rule.Different("22").is_different(22)
        failed_2 = Rule.Different(33).is_different(33)
        failed_3 = Rule.Different("22.3").is_different(22.3)
        failed_4 = Rule.Different(22.3).is_different(22.3)
        failed_5 = Rule.Different("str").is_different("str")

        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        self.assertTrue(passed_5)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)
        self.assertFalse(failed_5)

    def test_equal(self):
        passed_1 = Rule.Different("22").is_equal(22)
        passed_2 = Rule.Different(33).is_equal(33)
        passed_3 = Rule.Different("22.3").is_equal(22.3)
        passed_4 = Rule.Different(22.3).is_equal(22.3)
        passed_5 = Rule.Different("str").is_equal("str")

        failed_1 = Rule.Different("22").is_equal(23)
        failed_2 = Rule.Different(33).is_equal(34)
        failed_3 = Rule.Different("22.3").is_equal(22.4)
        failed_4 = Rule.Different(22.3).is_equal(22.4)
        failed_5 = Rule.Different("str").is_equal("str 1")

        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        self.assertTrue(passed_5)
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)
        self.assertFalse(failed_5)

    def test_gt(self):
        passed_1 = Rule.Different(21).gt("20")
        passed_2 = Rule.Different(20.2).gt("20.1")
        passed_3 = Rule.Different("string").gt("str")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        failed_1 = Rule.Different(19).gt("20")
        failed_2 = Rule.Different(20.1).gt("20.1")
        failed_3 = Rule.Different("string").gt("string")
        failed_4 = Rule.Different("21").gt("20")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)

    def test_gte(self):
        passed_1 = Rule.Different(21).gte("20")
        passed_1_1 = Rule.Different(20).gte("20")
        passed_2 = Rule.Different(20.2).gte("20.1")
        passed_2_1 = Rule.Different(20.2).gte("20.2")
        passed_3 = Rule.Different("string").gte("str")
        self.assertTrue(passed_1)
        self.assertTrue(passed_1_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_2_1)
        self.assertTrue(passed_3)
        failed_1 = Rule.Different(19).gte("20")
        failed_2 = Rule.Different("strin").gte("string")
        failed_3 = Rule.Different("19").gte("20")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

    def test_lt(self):
        passed_1 = Rule.Different(19).lt("20")
        passed_2 = Rule.Different(20.0).lt("20.1")
        passed_3 = Rule.Different("str").lt("string")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        failed_1 = Rule.Different(21).lt("20")
        failed_2 = Rule.Different(21.1).lt("20.1")
        failed_3 = Rule.Different("string").lt("str")
        failed_4 = Rule.Different("20").lt("20")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)

    def test_lte(self):
        passed_1 = Rule.Different(19).lte("20")
        passed_1_1 = Rule.Different(20).lte("20")
        passed_2 = Rule.Different(20.0).lte("20.1")
        passed_2_1 = Rule.Different(20.2).lte("20.2")
        passed_3 = Rule.Different("str").lte("str")
        self.assertTrue(passed_1)
        self.assertTrue(passed_1_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_2_1)
        self.assertTrue(passed_3)
        failed_1 = Rule.Different(21).lte("20")
        failed_2 = Rule.Different("string").lte("stri")
        failed_3 = Rule.Different("19").lte("20")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)

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
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {})

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
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'num_diff': ['The num_diff must be different to 233.'],
                                    'num_eq': ['The num_eq must be equal to 200.'],
                                    'num_gt': ['The num_gt must be greater than 100.'],
                                    'num_gte': ['The num_gte must be greater or equal to 199.'],
                                    'num_lt': ['The num_lt must be less than 100.'],
                                    'num_lte': ['The num_lte must be less or equal to 201.'],
                                    'str_diff': ['The str_diff must be different to MQ233.'],
                                    'str_eq': ['The str_eq must be equal to MQ200.'],
                                    'str_gt': ['The str_gt must be greater than MQ200.'],
                                    'str_gte': ['The str_gte must be greater or equal to MQ20.'],
                                    'str_lt': ['The str_lt must be less than abcdef.'],
                                    'str_lte': ['The str_lte must be less or equal to abcde.']})


if __name__ == '__main__':
    unittest.main()
