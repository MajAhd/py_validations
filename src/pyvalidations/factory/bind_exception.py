from .. import lang as Lang


class BindException:
    """
     Build validation messages when they are failed
     :param key data name
     :param value data value
    """

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def build(self, rule):
        """
        build failed message
        :param rule: name of validation
        :return: string
        """
        message = Lang.En(self.__key, self.__value).messages()
        return message[rule]
