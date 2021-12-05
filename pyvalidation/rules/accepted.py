class Accepted:
    """
    data value should be shown is accepted for instance : accept website rules
    """

    def __init__(self, value):
        self.value = value

    def is_accepted(self):
        """
        check value is accepted : on , yes , true , 1
        :return: Boolean
        """
        match self.value:
            case "on":
                is_passes = True
            case "yes":
                is_passes = True
            case "true":
                is_passes = True
            case True:
                is_passes = True
            case 1:
                is_passes = True
            case "1":
                return True
            case _:
                is_passes = False
        return is_passes
