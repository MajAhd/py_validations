from .en import En
from .de import De


class Languages:
    """
    Set and load validation messages
    """
    __key = None
    __value = None

    def __init__(self, lang_name="en"):
        self.lang_name = lang_name

    def set_key(self, key):
        """
        set message attribute name
        :return self
        """
        self.__key = key
        return self

    def set_value(self, value):
        """
        set message attribute value
        :return self
        """
        self.__value = value
        return self

    def messages(self):
        """
        Collection of Languages Support class to load messages
        """
        return {
            "en": En(self.__key, self.__value).messages(),
            "de": De(self.__key, self.__value).messages()
        }
