from ..lang import Languages


class BindException:
    """
     Build validation messages when they are failed
     :param key data name
     :param value data value
    """

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def build(self, rule, lang="en"):
        """
        build failed message
        :param rule: name of validation
        :return: string
        """
        message = Languages(lang) \
            .set_key(self.__key) \
            .set_value(self.__value) \
            .messages()[lang]
        return message[rule]
