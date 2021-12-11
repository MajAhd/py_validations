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
        - required_if:anotherField
         - The field under validation must be present and not empty if the anotherField field is
          exist and equal to any value.
        @param target : string
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
        :return: Boolean
        """
        if Field(self.__data, target).field_exist():
            required_value = self.__data[target]
            return not Required(required_value).is_required()
        return True

    def required_with(self, target):
        """
        :return: Boolean
        """
        return True

    def required_without(self, target):
        """

        :return: Boolean
        """
        return True
