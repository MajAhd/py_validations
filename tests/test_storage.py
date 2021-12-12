import os
import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestStorage(unittest.TestCase):

    def test_is_file(self):
        file = "img/PyValidation.png"
        passed_1 = Rule.Storage(file).is_file()
        passed_2 = Rule.Storage(file).max_size("20")
        passed_3 = Rule.Storage(file).min_size("10")
        passed_4 = Rule.Storage(file).mimes("png,jpg")
        passed_5 = Rule.Storage(file).mime_types("image/png,image/jpeg")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        self.assertTrue(passed_3)
        self.assertTrue(passed_4)
        self.assertTrue(passed_5)
        failed_1 = Rule.Storage("").is_file()
        failed_2 = Rule.Storage("ax.png").is_file()
        failed_3 = Rule.Storage(file).max_size("10")
        failed_4 = Rule.Storage(file).min_size("14")
        failed_5 = Rule.Storage(file).mimes("jpeg,jpg")
        failed_6 = Rule.Storage(file).mime_types("image/jpeg")
        self.assertFalse(failed_1)
        self.assertFalse(failed_2)
        self.assertFalse(failed_3)
        self.assertFalse(failed_4)
        self.assertFalse(failed_5)
        self.assertFalse(failed_6)

    def test_is_file_passed(self):
        data = {
            "avatar": "img/PyValidation.png",
        }
        rules = {
            "avatar": ["file", "mimes:png,jpeg", "mime_types:image/png,image/jpeg", "min_size:10", "max_size:20"],
        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_is_file_failed(self):
        data = {
            "avatar": "../img/PyValidation",
        }
        rules = {
            "avatar": ["file", "mimes:png,jpeg", "mime_types:image/png,image/jpeg", "min_size:10", "max_size:20"],
        }
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'failed': True,
            'errors': {
                'avatar': [
                    'The avatar must be a file.',
                    'The avatar must be a file of type: png,jpeg.',
                    'The avatar must be a file of type: image/png,image/jpeg.',
                    'The avatar  must be at least 10 kilobytes.',
                    'The avatar may not be greater than 20 kilobytes.'
                ]
            },
        })


if __name__ == '__main__':
    unittest.main()
