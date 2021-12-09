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
        return isinstance(self.value, str)

    def is_alpha(self):
        """
        Value must be alphabetic
        :return: bool
        """
        return re.match(r'^[A-Za-z]+$', self.value.replace(" ", ""))

    def start_with(self, target):
        """
        value mus start with target
        :param target: string
        :return: bool
        """
        if len(target) > len(self.value):
            return False
        return self.value[0:len(target)] == target

    def end_with(self, target):
        """
         Value must end with target
        :param target: string
        :return: bool
        """
        if len(target) > len(self.value):
            return False
        return self.value[len(target) * -1:] == target
