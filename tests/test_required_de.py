import unittest
import src.pyvalidations as PyValidation


class TestRequiredDe(unittest.TestCase):

    def test_pyvalidation_is_required(self):
        data = {
            "name_1": "Majid",
            "name_2": "",
            "name_3": None,
        }
        rules = {
            "name_1": ["required"],
            "name_2": ["required"],
            "name_3": ["required"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'name_2': ['Das Feld name_2 ist erforderlich.'],
                                               'name_3': ['Das Feld name_3 ist erforderlich.']},
                                    'failed': True})

    def test_required_if_passed(self):
        data = {
            "first_name": "",
            "last_name": "Ahmaditabar123",
            "age": "33",
        }
        rules = {
            "first_name": ["nullable", "alpha"],
            "last_name": ["required_if:first_name", "alpha"],
            "age": ["required_if:first_name", "numeric"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_required_if_failed(self):
        data = {
            "first_name": "Majid",
            "last_name": "Ahmaditabar123",
            "age": "",
        }
        rules = {
            "first_name": ["nullable", "alpha"],
            "last_name": ["required_if:first_name", "alpha"],
            "age": ["required_if:first_name", "numeric"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {
            'errors':
                {'age':
                     ['Das Feld age ist erforderlich, wenn first_name vorhanden ist.',
                      'Das age muss eine Zahl sein.'],
                 'last_name': ['Das last_name darf nur Buchstaben enthalten.']},
            'failed': True})

    def test_required_unless_passed(self):
        data = {
            "email": "example@email.com",
            "phone": "s123456",
        }
        rules = {
            "email": ["nullable", "email"],
            "phone": ["required_unless:email", "numeric"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_required_unless_failed(self):
        data = {
            "email": "",
            "phone": "s123456",
            "name": "",
        }
        rules = {
            "email": ["nullable", "email"],
            "phone": ["required_unless:email", "numeric"],
            "name": ["required_unless:email", "alpyha"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'name': ['Das Feld name ist erforderlich, es sei denn, email ist '
                                                        'nicht vorhanden oder leer.'],
                                               'phone': ['Das phone muss eine Zahl sein.']},
                                    'failed': True})

    def test_required_with_passed(self):
        data = {
            "first_name": "",
            "last_name": "Ahmaditabar123",
            "age": "33",
        }
        rules = {
            "first_name": ["nullable", "alpha"],
            "last_name": ["required_if:first_name", "alpha"],
            "age": ["required_with:first_name,last_name", "numeric"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_required_with_failed(self):
        data = {
            "first_name": "Majid",
            "last_name": "Ahmaditabar",
            "age": "",
        }
        rules = {
            "first_name": ["nullable", "alpha"],
            "last_name": ["nullable", "alpha"],
            "age": ["required_with:first_name,last_name", "numeric"],
        }

        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {
            'errors': {'age': ['Das Feld age ist erforderlich, wenn first_name,last_name vorhanden ist/sind.',
                               'Das age muss eine Zahl sein.']},
            'failed': True})

    def test_required_without_passed(self):
        data = {
            "email": "",
            "phone": "",
            "user_name": "MajAhd",
        }
        rules = {
            "email": ["nullable", "email"],
            "phone": ["nullable", "numeric"],
            "user_name": ["required_without:email,phone", "string"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_required_without_failed(self):
        data = {
            "email": "",
            "phone": "",
            "user_name": "",
        }
        rules = {
            "email": ["nullable", "email"],
            "phone": ["nullable", "numeric"],
            "user_name": ["required_without:email,phone", "string"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'user_name': ['Das Feld user_name ist erforderlich, wenn '
                                                             'email,phone nicht vorhanden ist/sind.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
