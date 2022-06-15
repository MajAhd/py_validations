import unittest
import src.pyvalidations as PyValidation


class TestUuidDe(unittest.TestCase):

    def test_pyvalidation_uuid_passed(self):
        data = {
            "uuid_1": "56b2724e-9074-4dc3-9803-4bb13c92ee0e",

        }
        rules = {
            "uuid_1": ["required", "uuid"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {}, 'failed': False})

    def test_pyvalidation_uuid_failed(self):
        data = {
            "uuid_1": "56b2-9074-4dc3-9803-4bb13c9",

        }
        rules = {
            "uuid_1": ["required", "uuid"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'failed': True,
                                    "errors": {
                                        'uuid_1': ['Das uuid_1 muss eine gültige UUID sein.']}
                                    })


if __name__ == '__main__':
    unittest.main()
