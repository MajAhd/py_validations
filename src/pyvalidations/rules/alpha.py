import re


class Alpha:
    """
    Validate Alphabetic data
    """

    def __init__(self, value):
        self.value = value

    def is_string(self):
        """
        value mus be a string
        :return: bool
        """
        try:
            return isinstance(self.value, str)
        except Exception:
            return False

    def is_alpha(self):
        """
        Value must be alphabetic
        :return: bool
        """
        try:
            return re.match(r'^[A-Za-z]+$', self.value.replace(" ", ""))
        except Exception:
            return False

    def start_with(self, target):
        """
        value mus start with target
        :param target: string
        :return: bool
        """
        try:
            if len(target) > len(self.value):
                return False
            return self.value[0:len(target)] == target
        except Exception:
            return False

    def end_with(self, target):
        """
         Value must end with target
        :param target: string
        :return: bool
        """
        try:
            if len(target) > len(self.value):
                return False
            return self.value[len(target) * -1:] == target
        except Exception:
            return False
