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
            if isinstance(self.value, int):
                try:
                    return self.value >= int(target)
                except ValueError:
                    return False

            if isinstance(self.value, float):
                try:
                    return self.value >= float(target)
                except ValueError:
                    return False
            return len(self.value) >= int(target)
        except Exception:
            return False
