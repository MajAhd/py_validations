class Field:
    """
    check data field (key) is existed
    """

    def __init__(self, all_data, req_field):
        self.__all_data = all_data
        self.__req_field = req_field

    def field_exist(self):
        """
        check key is in data
        :return: bool
        """
        if self.__req_field in self.__all_data:
            return True
        return False
