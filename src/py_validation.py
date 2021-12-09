import src.factory as Factory


class PyValidation:
    """
    start validate data by rules
    :param rules : collection of validation rules based on name
    :param data : collection of data
    """

    def __init__(self, data, rules):
        self.rules = rules
        self.data = data

    def make(self):
        """
        make validation
        :return: dictionary
        """
        validate = {
            "failed": False,
            "errors": {}
        }
        for name in self.data:
            key = name
            value = self.data[name]
            if key in self.rules:
                result = Factory.Validate(key, value, self.rules[key], self.data).validation()
                if len(result) > 0:
                    validate["failed"] = True
                    validate["errors"][key] = result
        return validate
