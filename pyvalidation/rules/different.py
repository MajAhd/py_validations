import re


class Different:
    """
    Check Value and target different logic
    """

    def __init__(self, value):
        self.value = value

    def is_different(self, target):
        """
        check target and value is different or not
        :return: bool
        """
        return str(self.value) != str(target)

    def is_equal(self, target):
        """
        check target and value is equal or not
        :return: bool
        """
        return str(self.value) == str(target)

    def gt(self, target):
        """
        check target and value is greater
        :return: bool
        """
        try:
            if str.isdigit(target):
                return self.value > int(target)
            if re.match(r'[+-]?([0-9]*[.])*[0-9]', str(target)):
                return self.value > float(target)
            return len(self.value) > len(target)
        except Exception:
            return False

    def gte(self, target):
        """
        check target and value is greater than or equal
        :return: bool
        """
        try:
            if str.isdigit(target):
                return self.value >= int(target)
            if re.match(r'[+-]?([0-9]*[.])*[0-9]', str(target)):
                return self.value >= float(target)
            return len(self.value) >= len(target)
        except Exception:
            return False

    def lt(self, target):
        """
        check target and value is greater
        :return: bool
        """
        try:
            if str.isdigit(target):
                return self.value < int(target)
            if re.match(r'[+-]?([0-9]*[.])*[0-9]', str(target)):
                return self.value < float(target)
            return len(self.value) < len(target)
        except Exception:
            return False

    def lte(self, target):
        """
        check target and value is greater
        :return: bool
        """
        try:
            if str.isdigit(target):
                return self.value <= int(target)
            if re.match(r'[+-]?([0-9]*[.])*[0-9]', str(target)):
                return self.value <= float(target)
            return len(self.value) <= len(target)
        except Exception:
            return False
