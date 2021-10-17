class Required:
    def __init__(self, value, data=None):
        if data is None:
            data = []
        self.__value = value
        self.__data = data

    """
      - is_required : check id field is empty , null 
      
    """

    def is_required(self):
        if self.__value is None or self.__value == "":
            return False
        else:
            return True

    def required_if(self):
        pass

    def required_unless(self):
        pass

    def required_with(self):
        pass

    def required_without(self):
        pass
