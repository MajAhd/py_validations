import unittest
import src.pyvalidations.rules as Rule
import src.pyvalidations as PyValidation


class TestFaPyValidation(unittest.TestCase):

    def test_pyvalidation_accepted(self):
        data = {
            "accept_6": "off",
            "accept_7": "false",
            "accept_8": "0",
        }
        rules = {
            "accept_6": ["required", "accepted"],
            "accept_7": ["required", "accepted"],
            "accept_8": ["required", "accepted"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'accept_6': ['accept_6 باید پذیرفته شود.'],
                                               'accept_7': ['accept_7 باید پذیرفته شود.'],
                                               'accept_8': ['accept_8 باید پذیرفته شود.']},
                                    'failed': True})

    def test_pyvalidation_alpha_failed(self):
        data = {
            "name": "John Doe 2021",
            "user_name": 920,
            "start_code": "G223other_string",
            "end_code": "other_stringG222"
        }
        rules = {
            "name": ["required", "alpha"],
            "user_name": ["required", "string"],
            "start_code": ["required", "start_with:G123"],
            "end_code": ["required", "end_with:G123"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'end_code': ['end_code باید با G123 ختم شود.'],
                                               'name': ['name باید فقط دارای حروف باشد.'],
                                               'start_code': ['start_code باید با G123 شروع شود.'],
                                               'user_name': ['user_nameباید از نوع متنی باشد. ']},
                                    'failed': True})

    def test_pyvalidation_boolean(self):
        data = {

            "bool_5": "1",
            "bool_6": "0",
            "bool_7": "false",
            "bool_8": "true",

        }
        rules = {

            "bool_5": ["required", "boolean"],
            "bool_6": ["required", "boolean"],
            "bool_7": ["required", "boolean"],
            "bool_8": ["required", "boolean"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'bool_5': ['مقدار bool_5  باید: true، false، 1 یا 0 باشد.'],
                                               'bool_6': ['مقدار bool_6  باید: true، false، 1 یا 0 باشد.'],
                                               'bool_7': ['مقدار bool_7  باید: true، false، 1 یا 0 باشد.'],
                                               'bool_8': ['مقدار bool_8  باید: true، false، 1 یا 0 باشد.']},
                                    'failed': True})

    def test_pyvalidation_confirmed(self):
        data_failed = {
            "password": "123456",
            "password_confirmed": "123456",
        }
        rules_2 = {
            "password": ["required", "confirmed"],
        }

        validate_failed = PyValidation.make(data_failed, rules_2, "fa")
        self.assertEqual(validate_failed,
                         {'errors': {'password': ['تأیید password مطابقت ندارد.']}, 'failed': True})

    def test_pyvalidation_datetime_failed(self):
        data = {
            "birthdate": "199004-17",
            "start_time": "1330",
            "expired": "2020-06-28-1220",
            "my_zone": "04:30",
        }
        rules = {
            "birthdate": ["required", "date"],
            "start_time": ["required", "time"],
            "expired": ["required", "datetime"],
            "my_zone": ["required", "timezone"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'birthdate': ['birthdate تاریخ معتبری نیست. '],
                                               'expired': ['expired تاریخ معتبری نیست.'],
                                               'my_zone': ['my_zone یک منطقه زمانی معتبر نیست. '],
                                               'start_time': ['start_time زمان معتبری نیست.']},
                                    'failed': True})

    def test_pyvalidation_datetime_different_failed(self):
        data = {
            "eq_bd": "1990-04-14",
            "after_bd": "1990-04-16",
            "after_equal_bd": "1990-04-15",
            "before_bd": "1990-04-17",
            "before_equal_bd": "1990-04-18",
        }
        rules = {
            "eq_bd": ["required", "date_equals:1990-04-17"],
            "after_bd": ["required", "after:1990-04-17"],
            "after_equal_bd": ["required", "after_or_equal:1990-04-17"],
            "before_bd": ["required", "before:1990-04-17"],
            "before_equal_bd": ["required", "before_or_equal:1990-04-17"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'after_bd': ['after_bd باید تاریخ بعد از 1990-04-17 باشد.'],
                                               'after_equal_bd': ['after_equal_bd باید تاریخ بعد یا برابر با '
                                                                  '1990-04-17 باشد.'],
                                               'before_bd': ['before_bd باید تاریخ قبل از 1990-04-17 باشد.'],
                                               'before_equal_bd': ['before_equal_bd باید تاریخ قبل یا برابر با '
                                                                   '1990-04-17 باشد.'],
                                               'eq_bd': ['eq_bd باید تاریخی برابر با 1990-04-17 باشد. ']},
                                    'failed': True})

    def test_pyvalidation_different_failed(self):
        data = {
            "num_diff": 233,
            "str_diff": "MQ233",
            "num_eq": 200,
            "str_eq": "MQ200",
            "num_gt": 100,
            "num_gte": 199,
            "str_gt": "MQ200",
            "str_gte": "MQ20",
            "num_lt": 100,
            "num_lte": 201,
            "str_lt": "abcdef",
            "str_lte": "abcde",
        }
        rules = {
            "num_diff": ["required", "different:233"],
            "str_diff": ["required", "different:MQ233"],
            "num_eq": ["required", "equal:100"],
            "str_eq": ["required", "equal:MQ100"],
            "num_gt": ["required", "gt:100"],
            "num_gte": ["required", "gte:200"],
            "str_gt": ["required", "gt:MQ200"],
            "str_gte": ["required", "gte:MQ200"],
            "num_lt": ["required", "lt:100"],
            "num_lte": ["required", "lte:200"],
            "str_lt": ["required", "lt:ABCD"],
            "str_lte": ["required", "lte:ABCD"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'num_diff': ['num_diff باید با 233 متفاوت باشد.'],
                                               'num_eq': ['num_eq باید برابر با 100 باشد.'],
                                               'num_gt': ['num_gt باید بزرگتر از 100 باشد.'],
                                               'num_gte': ['num_gte باید بزرگتر یا مساوی با 200 باشد.'],
                                               'num_lt': ['num_lt باید کمتر از 100 باشد. '],
                                               'num_lte': ['num_lte باید کمتر یا برابر با 200 باشد.'],
                                               'str_diff': ['str_diff باید با MQ233 متفاوت باشد.'],
                                               'str_eq': ['str_eq باید برابر با MQ100 باشد.'],
                                               'str_gt': ['str_gt باید بزرگتر از MQ200 باشد.'],
                                               'str_gte': ['str_gte باید بزرگتر یا مساوی با MQ200 باشد.'],
                                               'str_lt': ['str_lt باید کمتر از ABCD باشد. '],
                                               'str_lte': ['str_lte باید کمتر یا برابر با ABCD باشد.']},
                                    'failed': True})

    def test_pyvalidation_in_failed(self):
        data = {
            "north_america": "italy",
            "europe": "china",
            "grade": "u",
        }
        rules = {
            "north_america": ["required", "in:usa,canada"],
            "europe": ["required", "not_in:china,japan"],
            "grade": ["required", "in:a,b"],

        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'europe': ['europe انتخاب شده نامعتبر است.'],
                                               'grade': ['grade انتخاب شده نامعتبر است. '],
                                               'north_america': ['north_america انتخاب شده نامعتبر است. ']},
                                    'failed': True})

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
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'email': ['email باید یک آدرس ایمیل معتبر باشد. '],
                                               'ip': ['ip باید یک آدرس IP معتبر باشد. '],
                                               'ipv4': ['ipv4 باید یک آدرس IPv4 معتبر باشد.'],
                                               'ipv6': ['ipv6 باید یک آدرس IPv6 معتبر باشد.'],
                                               'url': ['url باید یک آدرس URL معتبر باشد.']},
                                    'failed': True})

    def test_pyvalidation_max_failed(self):
        data = {
            "age": 40,
        }
        rules = {
            "age": ["required", "max:30"],

        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'age': ['age نباید بزرگتر از 30 باشد. ']}, 'failed': True})

    def test_pyvalidation_min_failed(self):
        data = {
            "age": 17,
        }
        rules = {
            "age": ["required", "min:18"],

        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'age': ['age باید حداقل 18 باشد. ']}, 'failed': True})

    def test_pyvalidation_nullable_failed(self):
        data = {
            "name_1": "john 1",
            "number_2": "a2",
        }
        rules = {
            "name_1": ["nullable", "alpha"],
            "number_2": ["nullable", "numeric"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'name_1': ['name_1 باید فقط دارای حروف باشد.'],
                                               'number_2': ['number_2 باید یک عدد باشد. ']},
                                    'failed': True})

    def test_pyvalidation_number_failed(self):
        data = {
            "month": "a30",
            "year": 202,
        }
        rules = {
            "month": ["required", "numeric"],
            "year": ["required", "digits:4"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'month': ['month باید یک عدد باشد. '],
                                               'year': ['year باید رقم 4 باشد.']},
                                    'failed': True}
                         )

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
        validate = PyValidation.make(data, rules, "FA")
        self.assertEqual(validate, {'errors': {'name_2': [' فیلد name_2 الزامی است.'],
                                               'name_3': [' فیلد name_3 الزامی است.']},
                                    'failed': True})

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

        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'age': [' وقتی first_name وجود داشته باشد، فیلد  age  مورد نیاز '
                                                       'است.',
                                                       'age باید یک عدد باشد. '],
                                               'last_name': ['last_name باید فقط دارای حروف باشد.']},
                                    'failed': True})

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

        validate = PyValidation.make(data, rules, "Fa")
        self.assertEqual(validate, {'errors': {'name': ['فیلد  name مورد نیاز است مگر اینکه email وجود نداشته '
                                                        'باشد یا خالی باشد.'],
                                               'phone': ['phone باید یک عدد باشد. ']},
                                    'failed': True})

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

        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'age': ['فیلد age زمانی لازم است که first_name,last_name وجود '
                                                       'داشته باشد.',
                                                       'age باید یک عدد باشد. ']},
                                    'failed': True})

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
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'user_name': ['فیلد user_name زمانی لازم است که email,phone موجود '
                                                             'باشد/نیست.']},
                                    'failed': True})

    def test_pyvalidation_uuid_failed(self):
        data = {
            "uuid_1": "56b2-9074-4dc3-9803-4bb13c9",

        }
        rules = {
            "uuid_1": ["required", "uuid"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'uuid_1': ['uuid_1 باید یک UUID معتبر باشد.']}, 'failed': True})

    def test_is_file_failed(self):
        data = {
            "avatar": "../img/PyValidation",
        }
        rules = {
            "avatar": ["file", "mimes:png,jpeg", "mime_types:image/png,image/jpeg", "min_size:10", "max_size:20"],
        }
        validate = PyValidation.make(data, rules, "fa")
        self.assertEqual(validate, {'errors': {'avatar': ['avatar باید یک فایل باشد.',
                                                          'avatar باید فایلی از نوع: png,jpeg باشد.',
                                                          'avatar باید فایلی از نوع: image/png,image/jpeg باشد.',
                                                          'avatar باید حداقل 10 کیلوبایت باشد.',
                                                          'avatar نباید بیشتر از 20 کیلوبایت  باشد.']},
                                    'failed': True})


if __name__ == '__main__':
    unittest.main()
