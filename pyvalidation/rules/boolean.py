class Boolean:
    """
    Data Value must be Boolean
    """

    def __init__(self, value):
        self.value = value

    def is_boolean(self):
        """
        check value is boolean or 0 | 1
        :return: Boolean
        """
        if isinstance(self.value, bool):
            return True
        match self.value:
            case 1:
                is_passed = True
            case 0:
                is_passed = True
            case _:
                is_passed = False
        return is_passed
