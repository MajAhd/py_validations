class En:
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
            "field": f"The {self.attribute} is not exist",
            "required": f"The {self.attribute} field is required.",
            "required_if": f"The {self.attribute} field is required when {self.value} is exist.",
            "required_unless": f"The {self.attribute} field is required unless {self.value} is not exist or empty.",
            "required_with": f"The {self.attribute} field is required when {self.value} is/are present.",
            "required_without": f"The {self.attribute} field is required when {self.value} is/are not present.",
            "accepted": f"The {self.attribute} must be accepted.",
            "alpha": f"The {self.attribute} may only contain letters.",
            "boolean": f"The {self.attribute} may only boolean value : true , false , 1 or 0.",
            "string": f"The {self.attribute} may only string.",
            "start_with": f"The {self.attribute} may only start with {self.value}.",
            "end_with": f"The {self.attribute} may only end with {self.value}.",
            "numeric": f"The {self.attribute} must be a number.",
            "digits": f"The {self.attribute} must be {self.value} digits.",
            "max": f"The {self.attribute} may not be greater than {self.value}.",
            "min": f"The {self.attribute} must be at least {self.value}.",
            "email": f"The {self.attribute} must be a valid email address.",
            "url": f"The {self.attribute}  must be a valid URL address.",
            "ip": f"The {self.attribute} must be a valid IP address.",
            "ipv4": f"The {self.attribute} must be a valid IPv4 address.",
            "ipv6": f"The {self.attribute} must be a valid IPv6 address.",
            "in": f"The selected {self.attribute} is invalid.",
            "not_in": f"The selected {self.attribute} is invalid.",
            "uuid": f"The {self.attribute} must be a valid UUID.",
            "date": f"The {self.attribute} is not a valid date.",
            "time": f"The {self.attribute} is not a valid time.",
            "datetime": f"The {self.attribute} is not a valid datetime.",
            "timezone": f"The {self.attribute} is not a valid Timezone.",
            "date_equals": f"The {self.attribute} must be a date equal to {self.value}.",
            "after": f"The {self.attribute} must be a date after to {self.value}.",
            "after_or_equal": f"The {self.attribute} must be a date after or equal to {self.value}.",
            "before": f"The {self.attribute} must be a date before to {self.value}.",
            "before_or_equal": f"The {self.attribute} must be a date before or equal to {self.value}.",
            "different": f"The {self.attribute} must be different to {self.value}.",
            "equal": f"The {self.attribute} must be equal to {self.value}.",
            "gt": f"The {self.attribute} must be greater than {self.value}.",
            "gte": f"The {self.attribute} must be greater or equal to {self.value}.",
            "lt": f"The {self.attribute} must be less than {self.value}.",
            "lte": f"The {self.attribute} must be less or equal to {self.value}.",
            "confirmed": f"The {self.attribute} confirmation does not match.",
            "nullable": f"The {self.attribute} can be a null.",
            "file": f"The {self.attribute} must be a file.",
            "mimes": f"The {self.attribute} must be a file of type: {self.value}.",
            "mime_types": f"The {self.attribute} must be a file of type: {self.value}.",
            "max_size": f"The {self.attribute} may not be greater than {self.value} kilobytes.",
            "min_size": f"The {self.attribute}  must be at least {self.value} kilobytes.",
        }
