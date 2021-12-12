import os
import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation

os.path.exists('./img/PyValidation.png')


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
