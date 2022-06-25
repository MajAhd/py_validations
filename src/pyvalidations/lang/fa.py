class Fa:
    """
    Validation Exception message in English
    :param attribute : name of validation target
    :param value : value of attribute
    """

    def __init__(self, attribute, value):
        self.attribute = attribute
        self.value = value

    def messages(self):
        """
        validation messages
        :return: dict
        """
        return {
            "field": f"فیلد {self.attribute} وجود ندارد",
            "required": f" فیلد {self.attribute} الزامی است.",
            "required_if": f" وقتی {self.value} وجود داشته باشد، فیلد  {self.attribute}  مورد نیاز است.",
            "required_unless": f"فیلد  {self.attribute} مورد نیاز است مگر اینکه {self.value} وجود نداشته باشد یا خالی باشد.",
            "required_with": f"فیلد {self.attribute} زمانی لازم است که {self.value} وجود داشته باشد.",
            "required_without": f"فیلد {self.attribute} زمانی لازم است که {self.value} موجود باشد/نیست.",
            "accepted": f"{self.attribute} باید پذیرفته شود.",
            "alpha": f"{self.attribute} باید فقط دارای حروف باشد.",
            "boolean": f"مقدار {self.attribute}  باید: true، false، 1 یا 0 باشد.",
            "string": f"{self.attribute}باید از نوع متنی باشد. ",
            "start_with": f"{self.attribute} باید با {self.value} شروع شود.",
            "end_with": f"{self.attribute} باید با {self.value} ختم شود.",
            "numeric": f"{self.attribute} باید یک عدد باشد. ",
            "digits": f"{self.attribute} باید رقم {self.value} باشد.",
            "max": f"{self.attribute} نباید بزرگتر از {self.value} باشد. ",
            "min": f"{self.attribute} باید حداقل {self.value} باشد. ",
            "email": f"{self.attribute} باید یک آدرس ایمیل معتبر باشد. ",
            "url": f"{self.attribute} باید یک آدرس URL معتبر باشد.",
            "ip": f"{self.attribute} باید یک آدرس IP معتبر باشد. ",
            "ipv4": f"{self.attribute} باید یک آدرس IPv4 معتبر باشد.",
            "ipv6": f"{self.attribute} باید یک آدرس IPv6 معتبر باشد.",
            "in": f"{self.attribute} انتخاب شده نامعتبر است. ",
            "not_in": f"{self.attribute} انتخاب شده نامعتبر است.",
            "uuid": f"{self.attribute} باید یک UUID معتبر باشد.",
            "date": f"{self.attribute} تاریخ معتبری نیست. ",
            "time": f"{self.attribute} زمان معتبری نیست.",
            "datetime": f"{self.attribute} تاریخ معتبری نیست.",
            "timezone": f"{self.attribute} یک منطقه زمانی معتبر نیست. ",
            "date_equals": f"{self.attribute} باید تاریخی برابر با {self.value} باشد. ",
            "after": f"{self.attribute} باید تاریخ بعد از {self.value} باشد.",
            "after_or_equal": f"{self.attribute} باید تاریخ بعد یا برابر با {self.value} باشد.",
            "before": f"{self.attribute} باید تاریخ قبل از {self.value} باشد.",
            "before_or_equal": f"{self.attribute} باید تاریخ قبل یا برابر با {self.value} باشد.",
            "different": f"{self.attribute} باید با {self.value} متفاوت باشد.",
            "equal": f"{self.attribute} باید برابر با {self.value} باشد.",
            "gt": f"{self.attribute} باید بزرگتر از {self.value} باشد.",
            "gte": f"{self.attribute} باید بزرگتر یا مساوی با {self.value} باشد.",
            "lt": f"{self.attribute} باید کمتر از {self.value} باشد. ",
            "lte": f"{self.attribute} باید کمتر یا برابر با {self.value} باشد.",
            "confirmed": f"تأیید {self.attribute} مطابقت ندارد.",
            "nullable": f"{self.attribute} می تواند تهی باشد.",
            "file": f"{self.attribute} باید یک فایل باشد.",
            "mimes": f"{self.attribute} باید فایلی از نوع: {self.value} باشد.",
            "mime_types": f"{self.attribute} باید فایلی از نوع: {self.value} باشد.",
            "max_size": f"{self.attribute} نباید بیشتر از {self.value} کیلوبایت  باشد.",
            "min_size": f"{self.attribute} باید حداقل {self.value} کیلوبایت باشد.",
        }
