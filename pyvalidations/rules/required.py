class Required:
    """
     Required Validation
     check data is existed and has value on different rules
    """

    def __init__(self, value, data=None):
        if data is None:
            data = []
        self.__value = value
        self.__data = data

    def is_required(self):
        """
        data must exist and has value
        :return: Boolean
        """
        if self.__value is None or self.__value == "":
            return False
        return True

    def required_if(self):
        """

        :return: Boolean
        """
        return True

    def required_unless(self):
        """

        :return: Boolean
        """
        return True

    def required_with(self):
        """

        :return: Boolean
        """
        return True

    def required_without(self):
        """

        :return: Boolean
        """
        return True
