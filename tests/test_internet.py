import unittest
import src.rules as Rule
import src as PyValidation


class TestInternet(unittest.TestCase):

    def test_internet(self):
        email_passed = Rule.Internet("email@site.com").email()
        email_failed = Rule.Internet("email@com").email()
        self.assertTrue(email_passed)
        self.assertFalse(email_failed)
        url_passed_1 = Rule.Internet("http://www.google.com").url()
        url_passed_2 = Rule.Internet("https://google.com").url()
        url_passed_3 = Rule.Internet("https://google.com?search=python").url()
        url_failed_1 = Rule.Internet("google").url()
        url_failed_2 = Rule.Internet("google.com").url()
        self.assertTrue(url_passed_1)
        self.assertTrue(url_passed_2)
        self.assertTrue(url_passed_3)
        self.assertFalse(url_failed_1)
        self.assertFalse(url_failed_2)
        ip_passed_1 = Rule.Internet("8.8.8.8").ip()
        ip_passed_2 = Rule.Internet("0.0.0.0").ip()
        ip_failed = Rule.Internet("192168.1.1").ip()
        self.assertTrue(ip_passed_1)
        self.assertTrue(ip_passed_2)
        self.assertFalse(ip_failed)
        ipv4_passed = Rule.Internet("8.8.8.8").ipv4()
        ipv4_failed = Rule.Internet("192168.1.1").ipv4()
        self.assertTrue(ipv4_passed)
        self.assertFalse(ipv4_failed)
        ipv6_passed = Rule.Internet("2001:db8::1").ipv6()
        ipv6_failed = Rule.Internet("192168.1.1").ipv6()
        self.assertTrue(ipv6_passed)
        self.assertFalse(ipv6_failed)

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
        validate = PyValidation.PyValidation(data, rules).make()
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
        validate = PyValidation.PyValidation(data, rules).make()
        self.assertEqual(validate, {"failed": True,
                                    "errors": {
                                        'email': ['The email must be a valid email address.'],
                                        'ip': ['The ip must be a valid IP address.'],
                                        'ipv4': ['The ipv4 must be a valid IPv4 address.'],
                                        'ipv6': ['The ipv6 must be a valid IPv6 address.'],
                                        'url': ['The url  must be a valid URL address.']}
                                    })


if __name__ == '__main__':
    unittest.main()
