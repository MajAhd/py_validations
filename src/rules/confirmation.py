class Confirmation:
    """
     data value should be equal to target
     data   :   password
     target :   password_confirmation
     :param value  data value
     :param target data value to confirmation
    """
    def __init__(self, value, target):
        self.__value = value
        self.__target = target

    def is_confirmed(self):
        """
        check value and target equality
        :return: bool
        """
        return self.__value == self.__target
