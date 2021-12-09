class Number:
    """
    Check Value is number and validate Value len
    """

    def __init__(self, value):
        self.value = value

    def is_numeric(self):
        """
        check value is int / float
        :return: bool
        """
        try:
            return str.isdigit(str(self.value))
        except ValueError:
            return False

    def digits(self, length):
        """
        check value be digits
        :return: bool
        """
        try:
            return len(str(self.value)) == int(length)
        except ValueError:
            return False
