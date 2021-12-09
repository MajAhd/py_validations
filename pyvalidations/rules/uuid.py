import re


class Uuid:
    """
    Validate UUID format
    """

    def __init__(self, value):
        self.value = value

    def is_uuid(self):
        """
         value must be uuid format
         :return: bool
        """
        return self.uuid_rfc_4122()

    def uuid_rfc_4122(self):
        """
        RFC 4122
        - 0-9 or a-f 8 char
        - 0-9 or a-f 4 char
        - 0-9 or a-f 4 char
        - 0-9 or a-f 4 char
        - 0-9 or a-f 12 char
        :return: bool
        """
        return re.match(r'[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}', str(self.value))
