import unittest
import src.pyvalidations as PyValidation


class TestInternetDe(unittest.TestCase):

    def test_pyvalidation_internet_passed(self):
        data = {
            "email": "example@gmail.com",
            "url": "http://google.com",
            "ip": "192.168.1.1",
            "ipv4": "192.168.1.1",
            "ipv6": "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
        }
        rules = {
            "email": ["required", "email"],
            "url": ["required", "url"],
            "ip": ["required", "ip"],
            "ipv4": ["required", "ipv4"],
            "ipv6": ["required", "ipv6"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {"failed": False, "errors": {}})

    def test_pyvalidation_internet_failed(self):
        data = {
            "email": "example.gmail.com",
            "url": "google.com",
            "ip": "192.168.1",
            "ipv4": "192.168.1",
            "ipv6": "2001:0db8:85a3:0000:0000:8a2e:0370"
        }
        rules = {
            "email": ["required", "email"],
            "url": ["required", "url"],
            "ip": ["required", "ip"],
            "ipv4": ["required", "ipv4"],
            "ipv6": ["required", "ipv6"],
        }
        validate = PyValidation.make(data, rules, "de")
        self.assertEqual(validate, {'errors': {'email': ['Das email muss eine gültige E-Mail-Adresse sein.'],
                                               'ip': ['Das ip muss eine gültige IP-Adresse sein.'],
                                               'ipv4': ['Das ipv4 muss eine gültige IPv4-Adresse sein.'],
                                               'ipv6': ['The ipv6 must be a valid IPv6 address.'],
                                               'url': ['Das url muss eine gültige URL-Adresse sein.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
