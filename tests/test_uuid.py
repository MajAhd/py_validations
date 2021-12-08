import unittest
import pyvalidation.rules as Rule
import pyvalidation as PyValidation


class TestUuid(unittest.TestCase):

    def test_uuid(self):
        passed_1 = Rule.Uuid("56b2724e-9074-4dc3-9803-4bb13c92ee0e").is_uuid()
        failed_1 = Rule.Uuid("56b272-9074-4dc3-9803-4bb13c92ee0e").is_uuid()
        self.assertTrue(passed_1)
        self.assertFalse(failed_1)

    def test_pyvalidation_uuid_passed(self):
        data = {
            "uuid_1": "56b2724e-9074-4dc3-9803-4bb13c92ee0e",

        }
        rules = {
            "uuid_1": ["required", "uuid"],
        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {})

    def test_pyvalidation_uuid_failed(self):
        data = {
            "uuid_1": "56b2-9074-4dc3-9803-4bb13c9",

        }
        rules = {
            "uuid_1": ["required", "uuid"],
        }
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {'uuid_1': ['The uuid_1 must be a valid UUID.']})


if __name__ == '__main__':
    unittest.main()
