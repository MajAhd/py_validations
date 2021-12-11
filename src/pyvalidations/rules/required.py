from .field import Field


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

    def required_if(self, target):
        """
        The field under validation must be present and not empty if the anotherField field is
        exist and equal to any value.
        :param target : string
        :return: Boolean
        """
        if Field(self.__data, target).field_exist():
            required_value = self.__data[target]
            return Required(required_value).is_required()
        return False

    def required_unless(self, target):
        """
        The field under validation must be present and not empty unless the anotherField is
        Not Exist or be null or empty or "" value.
        :param target: string
        :return: Boolean
        """
        if Field(self.__data, target).field_exist():
            required_value = self.__data[target]
            return not Required(required_value).is_required()
        return True

    def required_with(self, target):
        """
        The field under validation must be present and not empty only if any of the other
        specified fields are present and not empty.
        :param target: string
        :return: Boolean
        """
        split_fields = target.split(",")
        res = True
        for field in split_fields:
            res &= self.required_if(field)
        return res

    def required_without(self, target):
        """
        The field under validation must be present and not empty only when any of the other specified fields
        are empty or not present.
        :param target: string
        :return: Boolean
        """
        split_fields = target.split(",")
        res = True
        for field in split_fields:
            res &= self.required_unless(field)
        return res
