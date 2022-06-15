import unittest
import src.pyvalidations as PyValidation


class TestStorageDe(unittest.TestCase):

    def test_is_file_passed(self):
        data = {
            "avatar": "img/PyValidation.png",
        }
        rules = {
            "avatar": ["file", "mimes:png,jpeg", "mime_types:image/png,image/jpeg", "min_size:10", "max_size:20"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_is_file_failed(self):
        data = {
            "avatar": "../img/PyValidation",
        }
        rules = {
            "avatar": ["file", "mimes:png,jpeg", "mime_types:image/png,image/jpeg", "min_size:10", "max_size:20"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'avatar': ['Das avatar muss eine Datei sein.',
                                                          'Das avatar muss eine Datei des Typs sein: png,jpeg.',
                                                          'Das avatar muss eine Datei des Typs sein: '
                                                          'image/png,image/jpeg.',
                                                          'Das avatar muss mindestens 10 Kilobyte groß sein.',
                                                          'Das avatar darf nicht größer als 20 Kilobyte sein.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
