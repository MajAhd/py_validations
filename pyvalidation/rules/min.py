class Min:
    """
    validate Minimum
    """

    def __init__(self, value):
        self.value = value

    def is_minimum(self, target):
        """
        value >= target
        :param target: string | number
        :return: bool
        """
        try:
            if str.isdigit(target):
                return self.value >= int(target)
            return False
        except Exception:
            return False
