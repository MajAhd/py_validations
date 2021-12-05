class Accepted:
    """
    data value should be acceptable : 0 , 1 , on , yes
    """
    def __init__(self, value):
        self.value = value

    def is_accepted(self):
        """
        :return: Boolean
        """
        return self.value
