class Inside:
    """
    check is value is in target or not
    value : any
    target : any
    """

    def __init__(self, value):
        self.value = str(value)

    def is_in(self, target):
        """
         check value in target
        :param target: any
        :return: bool
        """
        return self.value in target

    def is_not_in(self, target):
        """
        check value not in target
        :param target: any
        :return: bool
        """
        return self.value not in target
