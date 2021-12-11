import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestRequired(unittest.TestCase):

    def test_is_required(self):
        passed = Rule.Required("My Value").is_required()
        not_passed = Rule.Required("").is_required()
        null_value = Rule.Required(None).is_required()
        self.assertTrue(passed, "Required has value:  True")
        self.assertFalse(not_passed, "Required is empty : False")
        self.assertFalse(null_value, "Required is Null : False")

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
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {'failed': True,
                                    "errors": {
                                        'name_2': ['The name_2 field is required.'],
                                        'name_3': ['The name_3 field is required.']}
                                    })

    def test_required_if(self):
        data = {
            "first_name": "Majid",
        }
        passed = Rule.Required("doe", data).required_if("first_name")
        self.assertTrue(passed)
        failed = Rule.Required("", data).required_if("first_name_2")
        self.assertFalse(failed)

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

        validate = PyValidation.make(data, rules)
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

        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'errors': {'last_name': ['The last_name may only contain letters.'],
                       'age': ['The age field is required when first_name is exist.',
                               'The age must be a number.']},
            'failed': True})

    def test_required_unless(self):
        data = {
            "email": "example@email.com",
            "email_2": "",
        }
        passed_1 = Rule.Required("", data).required_unless("email_2")
        passed_2 = Rule.Required("123456", data).required_unless("email_3")
        self.assertTrue(passed_1)
        self.assertTrue(passed_2)
        failed_1 = Rule.Required("", data).required_unless("email")
        self.assertFalse(failed_1)

    def test_required_unless_passed(self):
        data = {
            "email": "example@email.com",
            "phone": "s123456",
        }
        rules = {
            "email": ["nullable", "email"],
            "phone": ["required_unless:email", "numeric"],
        }

        validate = PyValidation.make(data, rules)
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

        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'errors': {'name': ['The name field is required unless email is not exist or empty.'],
                       'phone': ['The phone must be a number.']
                       },
            'failed': True})

    def test_required_with(self):
        data = {
            "first_name": "John",
            "last_name": "doe",
            "full_name": "John Doe"
        }
        passed_1 = Rule.Required("John Doe", data).required_with("first_name,last_name")
        self.assertTrue(passed_1)
        failed_1 = Rule.Required("John Doe", data).required_with("name,family")
        self.assertFalse(failed_1)

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

        validate = PyValidation.make(data, rules)
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

        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'errors': {
                'age': [
                    'The age field is required when first_name,last_name is/are present.',
                    'The age must be a number.'
                ]
            },
            'failed': True})

    def test_required_without(self):
        data = {
            "email": "",
            "phone": "",
            "user_name": "MajAhd",
        }
        passed_1 = Rule.Required("John", data).required_without("email,phone")
        self.assertTrue(passed_1)
        data = {
            "email": "example@site.com",
            "phone": "12334555",
            "user_name": "MajAhd",
        }
        failed_1 = Rule.Required("John Doe", data).required_without("email,phone")
        self.assertFalse(failed_1)

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
        validate = PyValidation.make(data, rules)
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
        validate = PyValidation.make(data, rules)
        self.assertEqual(validate, {
            'errors': {'user_name': ['The user_name field is required when email,phone is/are not present.']},
            'failed': True})


if __name__ == '__main__':
    unittest.main()
