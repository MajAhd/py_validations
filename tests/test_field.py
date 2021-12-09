import unittest
import pyvalidations.rules as Rule


class TestField(unittest.TestCase):

    def test_different(self):
        data = {
            "name": "Majid",
            "job": "Developer",
        }
        passed_1 = Rule.Field(data, "name").field_exist()
        self.assertTrue(passed_1)
        failed_1 = Rule.Field(data, "age").field_exist()
        self.assertFalse(failed_1)


if __name__ == '__main__':
    unittest.main()
